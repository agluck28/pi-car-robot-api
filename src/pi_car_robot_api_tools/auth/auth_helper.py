import json
try:
    from common.request_response import make_request, make_response
except:
    from ..common.request_response import make_request, make_response

ADD_USER = {
    'queue': 'add_user',
    'make_request': (lambda email, password, access:
                     make_request(email=email,
                                  password=password,
                                  access=access)),
    'make_response': (lambda success, info=None:
                      make_response(success=success, info=info)),
    'decode_request': lambda request: json.loads(request),
    'decode_response': lambda response: json.loads(response)
}

AUTHENTICATE_USER = {
    'queue': 'authenticate_user',
    'make_request': (lambda email, password, access, life_span:
                     make_request(email=email,
                                  password=password,
                                  access=access,
                                  life_span=life_span)),
    'make_response': (lambda success, token=None, msg=None:
                      make_response(success, token=token, msg=msg)),
    'decode_request': lambda request: json.loads(request),
    'decode_response': lambda response: json.loads(response)
}

AUTHORIZE_USER = {
    'queue': 'authorize_user',
    'make_request': (lambda token, access:
                     make_request(token=token, access=access)),
    'make_response': (lambda success, valid, data=None:
                      make_response(success=success, valid=valid, data=data)),
    'decode_request': lambda request: json.loads(request),
    'decode_response': lambda response: json.loads(response)
}

DELETE_USER = {
    'queue': 'delete_user',
    'make_request': lambda email: make_request(email=email),
    'make_response': lambda success, msg: make_response(success=success, msg=msg),
    'decode_request': lambda request: json.loads(request),
    'decode_response': lambda response: json.loads(response)
}

GET_ALL_USERS = {
    'queue': 'get_all_users',
    'make_request': lambda: make_request(),
    'make_response': lambda success, users: make_response(success=success, users=users),
    'decode_request': lambda request: json.loads(request),
    'decode_response': lambda response: json.loads(response)
}

UPDATE_ACCESS = {
    'queue': 'update_access',
    'make_request': lambda email, access: make_request(email=email, access=access),
    'make_response': lambda success, info=None: make_response(success=success, info=info),
    'decode_request': lambda request: json.loads(request),
    'decode_response': lambda response: json.loads(response)
}

if __name__ == '__main__':

    print(ADD_USER['make_response'](True, 'test'))
