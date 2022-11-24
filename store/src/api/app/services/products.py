from app.database import dependencies
from app.database.crud import product
from pydantic import BaseModel

cursor = dependencies.get_connection()

#remover daqui
class ProductDTO(BaseModel):
  cpf: str
  nome: str
  sobrenome: str
  email: str
  telefone: str

def get_all():
    return product.find_all(cursor)

def create(dto: ProductDTO):
    return product.create(cursor, dto.id, dto.fabricacao_timestamp, dto.custo_unitario, dto.nome, dto.altura, dto.comprimento, dto.largura, dto.massa, dto.codigo_barra, dto.estoque)
