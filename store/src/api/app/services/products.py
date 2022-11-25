from app.database import dependencies
from app.database.crud import product
from pydantic import BaseModel

conn = dependencies.get_connection()

#remover daqui
class ProductDTO(BaseModel):
  cpf: str
  nome: str
  sobrenome: str
  email: str
  telefone: str

def get_all():
    return product.find_all(conn)

def get_by_id(id: str):
    return product.find_by_id(conn, id)

def create(dto: ProductDTO):
    return product.create(conn, dto.id, dto.fabricacao_timestamp, dto.custo_unitario, dto.nome, dto.altura, dto.comprimento, dto.largura, dto.massa, dto.codigo_barra, dto.estoque)

def delete(id: str):
    return product.delete_by_id(conn, id)
