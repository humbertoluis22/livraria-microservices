from sqlalchemy import create_engine
from usuario.shared.config.settings import Settings
from sqlalchemy import StaticPool # para nao criar sessoes atoa, aproveita sessoe criadas anteriormente 
from sqlalchemy.orm import Session

engine = create_engine(Settings().DATABASE_URL,pool_pre_ping=True,poolclass= StaticPool)

def get_session():
    with Session(bind=engine) as session:
        yield session

