from datetime import datetime
from typing import Optional
from sqlalchemy import DateTime, String, func, text
from sqlalchemy.orm import registry, Mapped, mapped_column
from uuid import UUID


table_registry = registry()


@table_registry.mapped_as_dataclass
class UsuarioModel:
    __tablename__ = "usuarios"

    uuid: Mapped[UUID] = mapped_column(String(100), primary_key=True)
    nome: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(150), unique=True)
    senha_hash: Mapped[str] = mapped_column(String(500))
    bloqueado: Mapped[bool] = mapped_column(nullable=False)
    criado_em: Mapped[datetime] = mapped_column(
        DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP")
    )
    atualizado_em: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
    
    @classmethod
    def from_entity(cls, entity: "Usuario") -> "Usuario":
        """Cria uma instância do Modelo a partir da Entidade de Domínio."""
        return cls(
            uuid=str(entity.uuid),
            nome=str(entity.nome),
            email=str(entity.email),
            senha_hash=str(entity.senha_hash),
            bloqueado=entity.bloqueado,
            criado_em=entity.criado_em,
            atualizado_em=entity.atualizado_em,
        )
