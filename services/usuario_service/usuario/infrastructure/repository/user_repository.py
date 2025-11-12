from infrastructure.models.usuario_model import UsuarioModel
from infrastructure.repository.base_repository import BaseRepository

class UserRepository(BaseRepository):
    def __init__(self):
        super().__init__(UsuarioModel)