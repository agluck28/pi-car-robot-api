from rpc_rabbitmq.RpcBaseRequest import RpcBaseRequest
from auth_helper import GET_ALL_USERS

class GetAllUsers(RpcBaseRequest):

    def __init__(self, RpcClient, timeout_ms: int = 1000):
        super().__init__(RpcClient, timeout_ms)
        self.routing_key = GET_ALL_USERS['queue']
        self.request = GET_ALL_USERS['make_request']()

    def make_request(self):
        return GET_ALL_USERS['decode_response'](super().make_request())
