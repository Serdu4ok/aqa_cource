from typing import Dict


class DataChecker:

    @staticmethod
    def check_created_board(board: Dict, response: Dict):
        assert board['id'] == response['id']
        assert board['name'] == response['name']
        assert board['desc'] == response['desc']
        assert board['descData'] == response['descData']
        assert board['idOrganization'] == response['idOrganization']
        assert board['pinned'] == response['pinned']
        assert board['url'] == response['url']
        assert board['shortUrl'] == response['shortUrl']
