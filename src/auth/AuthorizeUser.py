from rpc_rabbitmq.RpcBaseRequest import RpcBaseRequest
from auth_helper import AUTHORIZE_USER

class AuthorizeUser(RpcBaseRequest):

    def __init__(self, RpcClient, token: str, access: str, timeout_ms: int = 1000):
        super().__init__(RpcClient, timeout_ms)
        self.routing_key = AUTHORIZE_USER['queue']
        self.request = AUTHORIZE_USER['make_request'](token, access)

    def make_request(self):
        return  AUTHORIZE_USER['decode_response'](super().make_request())

