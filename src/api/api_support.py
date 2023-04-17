import json
import os
from typing import Dict

import requests
from requests import Response

from src.enum.sets import RequestType


class ApiSupport:

    def __init__(self):
        self._trello_url = os.getenv('TRELLO_URL')
        self._trello_key = os.getenv('TRELLO_KEY')
        self._trello_token = os.getenv('TRELLO_TOKEN')

    def _send_request(self, request_type: RequestType, url: str, query_params: Dict = None, expect_code: int = 200):
        params = self._create_params(query_params)
        response = requests.request(
            request_type,
            f'{self._trello_url}{url}',
            headers=self._get_headers(),
            params=params
        )

        self._check_status_code(response, expect_code)
        try:
            response_content = self._remove_dict_keys(json.loads(response.content))
        except json.JSONDecodeError:
            # If the response content is not JSON, but text
            response_content = response.content.decode('utf-8')

        return response_content

    @staticmethod
    def _get_headers() -> Dict:
        return {'Accept': 'application/json'}

    def _get_query_params(self) -> Dict:
        return {
            'key': self._trello_key,
            'token': self._trello_token
        }

    @staticmethod
    def _check_status_code(response: Response, expect_code: int = 200):
        actual_code = response.status_code
        assert actual_code == expect_code, f'Request URL: {response.request.url}\n' \
                                           f'Expected status code: {expect_code}\n' \
                                           f'Actual status code: {actual_code}\n' \
                                           f'Reason: {response.reason}\n' \
                                           f'Text: {response.text}'

    @staticmethod
    def _remove_dict_keys(my_dict: Dict) -> Dict:
        for key, value in list(my_dict.items()):
            if isinstance(value, dict):
                del my_dict[key]
        return my_dict

    def _create_params(self, query_params: Dict) -> Dict:
        if query_params:
            query_params.update(self._get_query_params())
        else:
            query_params = self._get_query_params()
        return query_params
