

from datetime import datetime
from uuid import UUID
from services.usuario_service.usuario.shared.utils.senhas import hash_password


class Usuario():
    def __init__(self,uuid,nome,email,senha,status):
        self.uuid = uuid
        self.nome = nome
        self.email = email
        self.senha_hash = hash_password(senha)
        self.staus = status
        self.criado_em = datetime.now()
        self.atualizado_em = None

