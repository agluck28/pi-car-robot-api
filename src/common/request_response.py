import json
import time

def make_request(**kwargs) -> str:
    request = {
        'time': time.time(),
    }
    if len(kwargs) > 0:
        for key, value in kwargs.items():
            if value is not None:
                if 'request_data' not in request:
                    request['request_data'] = {}
                request['request_data'][key] = value
    return json.dumps(request)

def make_response(success: bool, **kwargs) -> str:
    response = {
        'time': time.time(),
        'success': success
    }
    if len(kwargs) > 0:
        for key, value in kwargs.items():
            if value is not None:
                if 'response_data' not in response:
                    response['response_data'] = {}
                response['response_data'][key] = value
    return json.dumps(response)
