from rpc_rabbitmq.RpcBaseRequest import RpcBaseRequest
from auth_helper import DELETE_USER

class DeleteUser(RpcBaseRequest):

    def __init__(self, RpcClient, email: str, timeout_ms: int = 1000):
        super().__init__(RpcClient, timeout_ms)
        self.routing_key = DELETE_USER['queue']
        self.request = DELETE_USER['make_request'](email)

    def make_request(self):
        return DELETE_USER['decode_response'](super().make_request())