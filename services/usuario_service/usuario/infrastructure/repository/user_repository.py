from sqlalchemy import Select
from usuario.infrastructure.models.usuario_model import UsuarioModel
from usuario.infrastructure.repository.base_repository import BaseRepository

class UserRepository(BaseRepository):
    def __init__(self):
        super().__init__(UsuarioModel)
    
    def get_user_from_email(self,email):
        with self.get_session() as session:
            statement = Select(UsuarioModel).where(UsuarioModel.email == email)
            obj = session.execute(statement).scalar_one_or_none()
            return obj
    
    