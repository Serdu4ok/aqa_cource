from typing import Dict

from src.api.api_support import ApiSupport
from src.enum.sets import RequestType


class ApiActions(ApiSupport):
    def __init__(self):
        super().__init__()

    def create_board(self, name: str, expect_code: int = 200) -> Dict:
        query = {'name': name}
        return self._send_request(RequestType.POST, '/1/boards/', query, expect_code)

    def delete_board(self, board_id: str, expect_code: int = 200) -> Dict:
        return self._send_request(RequestType.DELETE, f'/1/boards/{board_id}', expect_code=expect_code)

    def get_board(self, board_id: str, expect_code: int = 200) -> Dict:
        return self._send_request(RequestType.GET, f'/1/boards/{board_id}', expect_code=expect_code)
