from rpc_rabbitmq.RpcBaseRequest import RpcBaseRequest
from auth_helper import UPDATE_ACCESS

class UpdateAccess(RpcBaseRequest):

    def __init__(self, RpcClient, email, access: list[str], timeout_ms: int = 1000):
        super().__init__(RpcClient, timeout_ms)
        self.routing_key = UPDATE_ACCESS['queue']
        self.request = UPDATE_ACCESS['make_request'](email, access)

    def make_request(self):
        return UPDATE_ACCESS['decode_response'](super().make_request())