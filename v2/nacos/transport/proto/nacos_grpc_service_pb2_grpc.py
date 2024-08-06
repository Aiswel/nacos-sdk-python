# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import nacos_grpc_service_pb2 as nacos__grpc__service__pb2


class RequestStreamStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.requestStream = channel.unary_stream(
                '/RequestStream/requestStream',
                request_serializer=nacos__grpc__service__pb2.Payload.SerializeToString,
                response_deserializer=nacos__grpc__service__pb2.Payload.FromString,
                )


class RequestStreamServicer(object):
    """Missing associated documentation comment in .proto file."""

    def requestStream(self, request, context):
        """build a streamRequest
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_RequestStreamServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'requestStream': grpc.unary_stream_rpc_method_handler(
                    servicer.requestStream,
                    request_deserializer=nacos__grpc__service__pb2.Payload.FromString,
                    response_serializer=nacos__grpc__service__pb2.Payload.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'RequestStream', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class RequestStream(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def requestStream(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/RequestStream/requestStream',
            nacos__grpc__service__pb2.Payload.SerializeToString,
            nacos__grpc__service__pb2.Payload.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class RequestStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.request = channel.unary_unary(
                '/Request/request',
                request_serializer=nacos__grpc__service__pb2.Payload.SerializeToString,
                response_deserializer=nacos__grpc__service__pb2.Payload.FromString,
                )


class RequestServicer(object):
    """Missing associated documentation comment in .proto file."""

    def request(self, request, context):
        """Sends a commonRequest
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_RequestServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'request': grpc.unary_unary_rpc_method_handler(
                    servicer.request,
                    request_deserializer=nacos__grpc__service__pb2.Payload.FromString,
                    response_serializer=nacos__grpc__service__pb2.Payload.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Request', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Request(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def request(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Request/request',
            nacos__grpc__service__pb2.Payload.SerializeToString,
            nacos__grpc__service__pb2.Payload.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class BiRequestStreamStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.requestBiStream = channel.stream_stream(
                '/BiRequestStream/requestBiStream',
                request_serializer=nacos__grpc__service__pb2.Payload.SerializeToString,
                response_deserializer=nacos__grpc__service__pb2.Payload.FromString,
                )


class BiRequestStreamServicer(object):
    """Missing associated documentation comment in .proto file."""

    def requestBiStream(self, request_iterator, context):
        """Sends a commonRequest
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_BiRequestStreamServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'requestBiStream': grpc.stream_stream_rpc_method_handler(
                    servicer.requestBiStream,
                    request_deserializer=nacos__grpc__service__pb2.Payload.FromString,
                    response_serializer=nacos__grpc__service__pb2.Payload.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'BiRequestStream', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class BiRequestStream(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def requestBiStream(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/BiRequestStream/requestBiStream',
            nacos__grpc__service__pb2.Payload.SerializeToString,
            nacos__grpc__service__pb2.Payload.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
