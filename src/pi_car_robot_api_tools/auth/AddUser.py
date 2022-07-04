from rpc_rabbitmq.RpcBaseRequest import RpcBaseRequest
from auth_helper import ADD_USER
from typing import Optional


class AddUser(RpcBaseRequest):

    def __init__(self, email: str, password: str,
                 access:str , RpcClient, timeout_ms: int = 1000):
        super().__init__(RpcClient, timeout_ms)
        self.routing_key = ADD_USER['queue']
        self.request = ADD_USER['make_request'](email, password, access)

    def make_request(self) ->  dict['success': bool, 'info': Optional[str]]:
        return ADD_USER['decode_response'](super().make_request())
