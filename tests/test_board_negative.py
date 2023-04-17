import pytest


class TestBoardNegative:

    @pytest.mark.negative
    def test_get_non_existent_board(self, api):
        response = api.get_board('643d3082aaf91e7b9e20656e', 404)
        assert response == 'The requested resource was not found.'

    @pytest.mark.negative
    def test_delete_non_existent_board(self, api):
        response = api.delete_board('643d3082aaf91e7b9e20656e', 404)
        assert response == 'The requested resource was not found.'
