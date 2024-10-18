import asyncio
import random

from v2.nacos.common.client_config import ClientConfig
from v2.nacos.common.constants import Constants
from v2.nacos.common.nacos_exception import NacosException, INVALID_PARAM, NOT_FOUND
from v2.nacos.nacos_client import NacosClient
from v2.nacos.naming.cache.service_info_cache import ServiceInfoCache
from v2.nacos.naming.model.instance import Instance
from v2.nacos.naming.model.naming_param import RegisterInstanceParam, BatchRegisterInstanceParam, \
    DeregisterInstanceRequest, ListInstanceRequest
from v2.nacos.naming.model.naming_request import SubscribeServiceRequest
from v2.nacos.naming.remote.naming_grpc_client_proxy import NamingGRPCClientProxy
from v2.nacos.naming.util.naming_client_util import get_service_cache_key, get_group_name


class NacosNamingService(NacosClient):
    def __init__(self, client_config: ClientConfig):
        super().__init__(client_config, Constants.NAMING_MODULE)
        self.namespace_id = client_config.namespace_id
        self.service_info_holder = ServiceInfoCache(client_config)
        self.grpc_client_proxy = NamingGRPCClientProxy(client_config, self.http_agent, self.service_info_holder)

    @staticmethod
    async def create_naming_service(client_config: ClientConfig) -> 'NacosNamingService':
        naming_service = NacosNamingService(client_config)
        await naming_service.grpc_client_proxy.start()
        return naming_service

    async def register_instance(self, request: RegisterInstanceParam) -> bool:
        if not request.service_name or not request.service_name.strip():
            raise NacosException(INVALID_PARAM, "service_name can not be empty")

        if not request.group_name:
            request.group_name = Constants.DEFAULT_GROUP

        if request.metadata is None:
            request.metadata = {}

        instance = Instance(ip=request.ip,
                            port=request.port,
                            metadata=request.metadata,
                            clusterName=request.cluster_name,
                            healthy=request.healthy,
                            enabled=request.enabled,
                            weight=request.weight,
                            ephemeral=request.ephemeral,
                            )

        instance.check_instance_is_legal()

        return await self.grpc_client_proxy.register_instance(request.service_name, request.group_name, instance)

    async def batch_register_instances(self, request: BatchRegisterInstanceParam) -> bool:
        if not request.service_name:
            raise NacosException(INVALID_PARAM, "service_name can not be empty")

        if not request.group_name:
            request.group_name = Constants.DEFAULT_GROUP

        if len(request.instances) == 0:
            raise NacosException(INVALID_PARAM, "instances can not be empty")

        instance_list = []
        for instance in request.instances:
            if not instance.ephemeral:
                raise NacosException(INVALID_PARAM,
                                     f"batch registration does not allow persistent instance:{instance}")
            instance_list.append(Instance(
                ip=instance.ip,
                port=instance.port,
                metadata=instance.metadata,
                clusterName=instance.cluster_name,
                healthy=instance.healthy,
                enable=instance.enable,
                weight=instance.weight,
                ephemeral=instance.ephemeral,
            ))

        return await self.grpc_client_proxy.batch_register_instance(request.service_name, request.group_name,
                                                                    instance_list)

    async def deregister_instance(self, request: DeregisterInstanceRequest) -> None:
        if not request.service_name:
            raise NacosException(INVALID_PARAM, "service_name can not be empty")

        if not request.group_name:
            request.group_name = Constants.DEFAULT_GROUP

        instance = Instance(ip=request.ip,
                            port=request.port,
                            cluster_name=request.cluster_name,
                            ephemeral=request.ephemeral,
                            )

        return await self.grpc_client_proxy.deregister_instance(request.service_name, request.group_name, instance)

    async def list_instances(self, request: ListInstanceRequest) -> list[Instance]:
        if not request.service_name:
            raise NacosException(INVALID_PARAM, "service_name can not be empty")

        if not request.group_name:
            request.group_name = Constants.DEFAULT_GROUP

        clusters = ",".join(request.clusters)

        service_info = None
        # 如果subscribe为true, 则优先从缓存中获取服务信息，并订阅该服务
        if request.subscribe:
            service_info = await self.service_info_holder.get_service_info(request.service_name, request.group_name,
                                                                           clusters)
        if service_info is None:
            service_info = await self.grpc_client_proxy.subscribe(request.service_name, request.group_name, clusters)

        instance_list = []
        if service_info is not None and len(service_info.hosts) > 0:
            instance_list = service_info.hosts

        # 如果设置了healthy_only参数,表示需要查询健康或不健康的实例列表，为true时仅会返回健康的实例列表，反之则返回不健康的实例列表。默认为None
        if request.healthy_only is not None:
            instance_list = list(
                filter(lambda host: host.healthy == request.healthy_only and host.enabled and host.weight > 0,
                       instance_list))

        return instance_list

    async def subscribe(self, request: SubscribeServiceRequest, call_back_func) -> None:
        if not request.service_name:
            raise NacosException(INVALID_PARAM, "service_name can not be empty")

        if not request.group_name:
            request.group_name = Constants.DEFAULT_GROUP

        clusters = ",".join(request.clusters)


        self.service_info_holder.register_callback(, call_back_func)
    # def update_instance(self, request: UpdateInstanceRequest):
    #     if not request.service_name or not request.serviceName.strip():
    #         raise NacosException(INVALID_PARAM, "service_name can not be empty")
    #
    #     if not request.group_name:
    #         request.group_name = Constants.DEFAULT_GROUP
    #
    #     if request.metadata is None:
    #         request.metadata = {}
    #
    #     instance = Instance(ip=request.ip,
    #                         port=request.port,
    #                         metadata=request.metadata,
    #                         cluster_name=request.cluster_name,
    #                         healthy=request.healthy,
    #                         enable=request.enable,
    #                         weight=request.weight,
    #                         ephemeral=request.ephemeral,
    #                         )
    #
    #     instance.check_instance_is_legal()
    #
    #     return self.client_proxy_delegate.register_instance(request.service_name, request.group_name, instance)

    def get_all_instances(self):
        pass

    def select_instances(self):
        pass

    def select_one_healthy_instance(self):
        pass

    def subscribe(self):
        pass

    def unsubscribe(self):
        pass

    def get_services_of_server(self):
        pass

    def get_server_status(self) -> str:
        pass

    def shutdown(self) -> None:
        pass
