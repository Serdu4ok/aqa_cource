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
