from fastapi import FastAPI
from usuario.api.middleware.response_middleware import response_standardize_middleware
from usuario.api.controller import usuario_controller 
from starlette.middleware.base import BaseHTTPMiddleware

app = FastAPI()
# app.mount('http')(response_standardize_middleware)
# app.add_middleware(BaseHTTPMiddleware, dispatch=response_standardize_middleware)

app.include_router(usuario_controller.router)
