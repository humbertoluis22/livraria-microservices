from usuario.infrastructure.repository.user_repository import UserRepository
from usuario.domain.entitie.usuario_entitie import Usuario
from usuario.infrastructure.models.usuario_model import (
    UsuarioModel,
)
from usuario.shared.dtos.request.usuario_request import (
    UsuarioRequest,
)
import uuid


class UsuarioService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository


    def cadastrar_usuario(self, user_info: UsuarioRequest):
        info_user_db: UsuarioModel = self.user_repository.get_user_from_email(
            user_info.email
        )
        if info_user_db.email == user_info.email or info_user_db.nome == user_info.nome:
            raise ValueError("Email ja utilizado")
        uuid_user = uuid.uuid4()
        usuario = Usuario(
            uuid=str(uuid_user),
            nome=user_info.nome,
            email=user_info.email,
            senha=user_info.senha,
        )
        usuario_db = UsuarioModel.from_entity(usuario)
        self.user_repository.create(usuario_db)
        return uuid_user

    def recolher_usuarios(self):
        return self.user_repository.get_all()

    def desbloquear_usuario(self, uuid):
        usuario_db: UsuarioModel = self.user_repository.get_attribute_by_uuid(uuid)
        if usuario_db:
            if usuario_db.bloqueado:
                self.user_repository.update_attribute_by_id(uuid, "bloqueado", False)
                return 'Usuario desbloqueado'
            else:
                raise ValueError("O usuario informado nao esta bloqueado")
        raise ValueError("Nenhum usuario cadastrado com esse valor")


    def excluir_usuario(self,uuid:uuid.UUID):
        self.user_repository.delete(uuid)
        return f"Usuario com uuid {uuid} deletado"

def get_usuario_service() -> UsuarioService:
    repo = UserRepository()
    return UsuarioService(repo)
