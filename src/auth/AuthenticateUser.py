from rpc_rabbitmq.RpcBaseRequest import RpcBaseRequest
from auth_helper import AUTHENTICATE_USER


class AuthenticateUser(RpcBaseRequest):

    def __init__(self, RpcClient, email: str,
                 password: str, access: str, life_span: int, timeout_ms: int = 1000):
        super().__init__(RpcClient, timeout_ms)
        self.routing_key = AUTHENTICATE_USER['queue']
        self.request = AUTHENTICATE_USER['make_request'](email,
                                                         password,
                                                         access,
                                                         life_span)

    def make_request(self):
        return AUTHENTICATE_USER['decode_response'](super().make_request())
