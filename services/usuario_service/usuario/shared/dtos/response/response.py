from http import HTTPStatus
from time import time


def wrap_response(
    data, message='Operação realizada com sucesso!', status=HTTPStatus.OK
):
    return {
        'status': status,
        'message': message,
        'result': data,
        'timestamp': int(time()),
    }
