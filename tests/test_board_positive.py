import pytest
import requests

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
        api.get_board(board['id'])
        # self.data_checker.check_created_board(board, response)
        response = api.delete_board(board['id'])
        print(response)

    def test_get_cached_board(self, api, get_created_board):
        board = get_created_board
        print(board)




    def test_api_board(self):
        url = "https://api.trello.com/1/boards/"

        query = {
            'name': 'test name meet',
            'key': '48859f892926f3af3c74581d0c894f63',
            'token': '15daea39866e0cb2c339a4369dd8ef5b829f493d6f32a0e4a78625c1e8be8092'
        }

        response = requests.request(
            "POST",
            url,
            params=query
        )

        print(response.text)
