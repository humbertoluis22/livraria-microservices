from typing import Any
from uuid import UUID
from sqlalchemy import Select
from sqlalchemy.orm import Session
from usuario.shared.config.database import get_session as default_session

class BaseRepository:
    def __init__(self,model):
        self.model = model 
    
    def get_session(self) -> Session:
        """
        Método interno que retorna a sessão do banco.
        Pode ser sobrescrito ou mockado em testes.
       """
        return default_session()
    
    def create(self,instance):
        with self.get_session() as session:
            session.add(instance)
            session.commit()
    

    def get_all(self):
        with self.get_session() as session:
            objs = session.query(self.model).all()
            return objs
    

    def get_attribute_by_uuid(self,uuid:UUID):
        with self.get_session() as session:
            obj = session.get(self.model,str(uuid))
            return obj
        
    def update_attribute_by_id(self,uuid:UUID,column_name:str,value:Any):
        if not hasattr(self.model,column_name):
            print(f'tentativa de atualizar atributo inexistente {column_name} no modelo {self.model}')

        with self.get_session() as session:
            obj = session.get(self.model,str(uuid))
            if obj:
                setattr(obj,column_name,value)
                session.commit()
            else:
                print(f'Registro com uuid: {uuid} nao encontrado para atualizacao de {column_name}')

    def delete(self,uuid:UUID):
        with self.get_session() as session:
            obj = session.get(self.model,uuid)
            if obj:
                session.delete(obj)
                session.commit()
            else:
                print(f'tentativa de deletar registro com o UUID: {uuid}, mas nao foi encontrado')