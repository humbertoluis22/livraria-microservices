from datetime import datetime
from sqlalchemy import String,func
from sqlalchemy.orm import registry,Mapped,mapped_column
from uuid import UUID

table_registry = registry()

@table_registry.mapped_as_dataclass
class Usuario:
    __tablename__ = "usuarios"

    id:Mapped[UUID] = mapped_column(primary_key=True,autoincrement=True,init=False)
    nome:Mapped[str] = mapped_column(String(100))
    email:Mapped[str] = mapped_column(String(150),unique=True)
    senha_hash:Mapped[str] = mapped_column(String(500))
    status:Mapped[str] = mapped_column(String(12))
    criado_em:Mapped[datetime] = mapped_column(init=False,server_default=func.now())
    atualizado_em:Mapped[datetime] = mapped_column()