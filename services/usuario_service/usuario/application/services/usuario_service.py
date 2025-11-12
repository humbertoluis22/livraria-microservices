from infrastructure.repository.user_repository import UserRepository

class UsuarioService():
    def __init__(self, user_repository : UserRepository):
        self.user_repository = user_repository


def  get_usuario_service() -> UsuarioService:
    repo = UserRepository()
    return UsuarioService(repo)
    