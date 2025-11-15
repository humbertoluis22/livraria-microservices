from pydantic import BaseModel, EmailStr

class UsuarioRequest(BaseModel):
    nome: str
    email: EmailStr
    senha: str
