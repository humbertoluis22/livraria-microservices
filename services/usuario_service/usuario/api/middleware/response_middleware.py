import json
import time
from http import HTTPStatus

from fastapi import Request
from fastapi.responses import JSONResponse
import logging  

# logger = logger.getChild(__name__)
logger = logging.getLogger(__name__)

# Rotas que não devem ser interceptadas
EXCLUDED_PATHS = ['/docs', '/redoc', '/openapi.json', '/favicon.ico']


async def response_standardize_middleware(request: Request, call_next):
    # Ignora rotas do Swagger e outras estáticas
    if any(request.url.path.endswith(path) for path in EXCLUDED_PATHS):
        return await call_next(request)

    try:
        response = await call_next(request)

        # Verifica se é uma resposta JSON
        content_type = response.headers.get('content-type', '')
        if 'application/json' not in content_type:
            return response

        # Lê o corpo da resposta
        body = b''
        async for chunk in response.body_iterator:
            body += chunk

        # Tenta decodificar o corpo
        try:
            payload = json.loads(body)
        except json.JSONDecodeError:
            payload = body.decode()

        status_code = response.status_code

        # Retorna resposta padronizada
        return JSONResponse(status_code=status_code, content=payload)

    except ValueError as ve:
        error_msg = (
            f'Conflito gerado na requisição: {request.method} '
            f'{request.url.path} - Erro: {ve}'
        )
        logger.warning(error_msg)
        return JSONResponse(
            status_code=HTTPStatus.CONFLICT,
            content={
                'status': HTTPStatus.CONFLICT,
                'message': f'Conflito gerado: {str(ve)}',
                'result': None,
                'timestamp': int(time.time()),
            },
        )

    except Exception as ex:
        error_msg = (
            f'Erro interno inesperado na requisição: {request.method} '
            f'{request.url.path} - Erro: {ex}'
        )
        logger.error(error_msg)
        return JSONResponse(
            status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
            content={
                'status': HTTPStatus.INTERNAL_SERVER_ERROR,
                'message': 'Ocorreu um erro interno inesperado no servidor.',
                'result': None,
                'timestamp': int(time.time()),
            },
        )
