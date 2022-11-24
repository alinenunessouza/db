from app.database import dependencies
from app.database.crud import user
from pydantic import BaseModel

cursor = dependencies.get_connection()

#remover daqui
class UserDTO(BaseModel):
  cpf: str
  nome: str
  sobrenome: str
  email: str
  telefone: str

def get_all():
    return user.find_all(cursor)

def create(dto: UserDTO):
    return user.create(cursor, dto.cpf, dto.nome, dto.sobrenome, dto.email, dto.telefone)
