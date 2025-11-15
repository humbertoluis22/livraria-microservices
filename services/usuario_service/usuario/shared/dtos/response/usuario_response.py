from datetime import datetime
from typing import Literal, Optional
from uuid import UUID

from pydantic import BaseModel, ConfigDict, EmailStr
from usuario.shared.dtos.response.result_response import ResponseData

class UserSchema(BaseModel):
    uuid: UUID
    nome: str
    email: EmailStr
    bloqueado: bool
    criado_em: datetime

    model_config = ConfigDict(from_attributes=True)

class UsuariosResult(BaseModel):
    usuarios: Optional[list[UserSchema]] = None


class Usuarios(ResponseData):
    result: UsuariosResult



class UsuarioDesbloqueadoResult(BaseModel):
    status: str
    

class DeletarUsuarioResult(BaseModel):
    status: str
    
class UsuarioCriadoResult(BaseModel):
    usuario_criado : UUID | bool

class UsuarioCriado(ResponseData):
    result : UsuarioCriadoResult