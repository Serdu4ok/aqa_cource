from enum import Enum


class RequestType(str, Enum):
    GET = 'Get'
    OPTIONS = 'Options'
    HEAD = 'Head'
    POST = 'Post'
    PUT = 'Put'
    PATCH = 'Patch'
    DELETE = 'Delete'


FACTORIAL = ((0, 1),
             (1, 1),
             (2, 2),
             (3, 6),
             (4, 24),
             (5, 120),
             (6, 720))


class ApiErrors(str, Enum):
    NOT_FOUND = 'The requested resource was not found.'


class TestData(str, Enum):
    INCORRECT_ID = '643d3082aaf91e7b9e20656e'


