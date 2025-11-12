from datetime import datetime
from sqlalchemy import String,func
from sqlalchemy.orm import registry,Mapped,mapped_column
from uuid import UUID


table_registry = registry()

@table_registry.mapped_as_dataclass
class UsuarioModel:
    __tablename__ = "usuarios"

    uuid:Mapped[UUID] = mapped_column(primary_key=True,autoincrement=True,init=False)
    nome:Mapped[str] = mapped_column(String(100))
    email:Mapped[str] = mapped_column(String(150),unique=True)
    senha_hash:Mapped[str] = mapped_column(String(500))
    status:Mapped[str] = mapped_column(String(12))
    criado_em:Mapped[datetime] = mapped_column(init=False,server_default=func.now())
    atualizado_em:Mapped[datetime] = mapped_column()

    @classmethod
    def from_entity(cls, entity: 'Usuario') -> 'Usuario':
        """Cria uma instância do Modelo a partir da Entidade de Domínio."""
        return cls(
            uuid=str(entity.uuid),
            nome = str(entity.nome),
            email = str(entity.email),
            senha_hash = str(entity.senha_hash),
            staus = str(entity.status),
            criado_em = str(entity.criado_em),
            atualizado_em =str(entity.atualizado_em)
        )
