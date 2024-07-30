import time
import json


def get_current_time_millis():
    t = time.time()
    return int(round(t * 1000))


def to_json_string(obj):
    try:
        return json.dumps(obj)
    except (TypeError, ValueError) as e:
        print(f"Error serializing object to JSON: {e}")
        return None