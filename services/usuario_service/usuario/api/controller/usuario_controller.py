from fastapi import APIRouter, Depends
from uuid import UUID

from usuario.application.services.usuario_service import (
    UsuarioService,
    get_usuario_service,
)
from usuario.shared.dtos.request.usuario_request import UsuarioRequest
from usuario.shared.dtos.response.usuario_response import (
    DeletarUsuarioResult,
    UsuarioCriado,
    UsuarioCriadoResult,
    UsuarioDesbloqueadoResult,
    Usuarios,
    UsuariosResult
    
)


router = APIRouter(prefix="/usuario", tags=["Usuario"])


@router.post("/criar_usuario", response_model=UsuarioCriadoResult)
def criar_usuario(
    user_info:UsuarioRequest,
    usuario_service: UsuarioService = Depends(get_usuario_service),
):
    return {'usuario_criado':usuario_service.cadastrar_usuario(user_info)
}


@router.get('/recolher_usuarios',response_model=UsuariosResult)
def recolher_usuarios(usuario_service:UsuarioService = Depends(get_usuario_service)):
    return{"usuarios":usuario_service.recolher_usuarios()}


@router.put('/desbloquear_usuario/{uuid}',response_model=UsuarioDesbloqueadoResult)
def desbloquear_usuario(uuid,usuario_service:UsuarioService = Depends(get_usuario_service)):
    return {'status':usuario_service.desbloquear_usuario(uuid)}

@router.delete('/excluir_usuario/{uuid}',response_model=DeletarUsuarioResult)
def excluir_usuario(uuid,usuario_service:UsuarioService = Depends(get_usuario_service)):
    return {'status': usuario_service.excluir_usuario(uuid)}