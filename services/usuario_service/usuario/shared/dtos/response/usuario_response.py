from datetime import datetime
from typing import Literal, Optional
from uuid import UUID

from pydantic import BaseModel
from shared.dtos.response.result_response import ResponseData


class UsuariosResult(BaseModel):
    usuarios: Optional[list[str]] = None


class Usuarios(ResponseData):
    result: UsuariosResult


class UsuarioCriadoResult(BaseModel):
    usuario_criado : UUID | bool

class UsuarioCriado(ResponseData):
    result : UsuarioCriadoResult