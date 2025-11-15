

from datetime import datetime
from uuid import UUID
from usuario.shared.utils.senhas import hash_password
import re


class Usuario():
    def __init__(self,uuid,nome,email,senha):
        self.uuid = uuid
        self.nome = self.__valida_nome(nome)
        self.email = self.__valida_email(email)
        self.senha_hash = self.__valida_senha(senha)    
        self.bloqueado = False
        self.criado_em = datetime.now()
        self.atualizado_em = None

    def __valida_nome(self,nome:str)->str:
        if  not (len(nome) >=3 and len(nome) <=  100):
            raise ValueError("Nome precisa conter entre 3 e 100 caracteres")
        return nome

    def __valida_senha(self,senha:str) -> str:
        pattern = r"""^(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*()\-_=+{}[\]|\\:;\'<>,.?/]).{8,}$"""
        if not re.match(pattern,senha):
            raise ValueError("Senha precisa conter no minimo 8 caracteres, um letra maiscula , caracter especial e numero") 
        
        return hash_password(senha)

    def __valida_email(self,email:str) -> str:
        pattern = r"""^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"""
        if not re.match(pattern,email):
            raise ValueError("Informe um endereço de email valido")
        
        return email