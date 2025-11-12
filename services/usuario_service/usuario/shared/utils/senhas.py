from typing import Union
import bcrypt

def hash_password(password: Union[str, bytes]) -> str:
    """
    Gera um hash seguro para a senha usando bcrypt.
    Retorna o hash codificado em utf-8 (string) pronto para armazenar no banco.
    bcrypt já gera um salt único por hash internamente.
    """
    if isinstance(password, str):
        password = password.encode("utf-8")
    salt = bcrypt.gensalt()  
    hashed = bcrypt.hashpw(password, salt)
    return hashed.decode("utf-8")

def verify_password(password: Union[str, bytes], hashed: Union[str, bytes]) -> bool:
    """
    Verifica se 'password' coincide com o 'hashed' (hash gerado pelo hash_password).
    Retorna True se bater, False caso contrário.
    """
    if isinstance(password, str):
        password = password.encode("utf-8")
    if isinstance(hashed, str):
        hashed = hashed.encode("utf-8")
    return bcrypt.checkpw(password, hashed)

if __name__ == "__main__":
    senha = hash_password('senha mt boa')
    print(senha)
    print(verify_password('senha mt boa',senha))
    print(verify_password('senha errada',senha))