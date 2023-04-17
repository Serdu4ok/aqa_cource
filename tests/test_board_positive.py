import pytest

from src.data_checker import DataChecker


class TestBoardPositive:

    @pytest.fixture(autouse=True)
    def pre_test(self):
        self.data_checker = DataChecker

    def test_create_board(self, api):
        board = api.create_board('test 1')
        response = api.get_board(board['id'])
        assert board['id'] == response['id']
        assert board['name'] == response['name']
        assert board['desc'] == response['desc']
        assert board['descData'] == response['descData']
        assert board['idOrganization'] == response['idOrganization']
        assert board['pinned'] == response['pinned']
        assert board['url'] == response['url']
        assert board['shortUrl'] == response['shortUrl']
        api.delete_board(board['id'])

    def test_create_board_2(self, api):
        board = api.create_board('test 1')
        response = api.get_board(board['id'])
        self.data_checker.check_created_board(board, response)
        api.delete_board(board['id'])

    def test_get_cached_board(self, api, get_created_board):
        board = get_created_board
        print(board)
