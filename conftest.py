import os
from typing import Dict

import dotenv
import pytest
from dotenv import load_dotenv

from src.api.api import ApiActions

dotenv.load_dotenv('.env.local')


def set_env_variables():
    root_path = os.path.dirname(os.path.abspath(__file__))
    os.environ['ROOT_PATH'] = root_path
    load_dotenv(dotenv_path=f'{root_path}/.env.local')


set_env_variables()


@pytest.fixture(autouse=True)
def api(request) -> ApiActions:  # pylint: disable=unused-argument
    main_api = ApiActions()
    yield main_api


@pytest.fixture(scope='session')
def get_created_board() -> Dict:
    board = ApiActions().create_board('Fixture board')
    yield board
    ApiActions().delete_board(board['id'])
