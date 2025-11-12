from fastapi import APIRouter,Depends
from uuid import UUID

from services.usuario_service.usuario.application.services.usuario_service import get_usuario_service
from services.usuario_service.usuario.shared.dtos.response.usuario_response import UsuarioCriado, Usuarios


router = APIRouter(prefix='/virtual_agent_b2k', tags=['Agente Virtual B2K'])


@router.post('/criar_usuario',response_class=UsuarioCriado)
def criar_usuario(usuario_service = Depends(get_usuario_service)):
    return usuario_service.cadastrar_usuario()

# @router.get('/get_users',response_model=Usuarios)
# def  