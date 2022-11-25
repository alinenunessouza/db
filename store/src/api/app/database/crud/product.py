from app.database.models.product import Product
import datetime

def find_all(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Produto")
    result = []
    for item in cursor.fetchall():
        result.append(
            Product(
                item[0],
                item[1],
                item[2],
                item[3],
                item[4],
                item[5],
                item[6],
                item[7],
                item[8],
                item[9],
            )
        )
    return result

def find_by_id(conn, id:str):
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM Produto WHERE id = '{id}'")
    result = cursor.fetchone()
    return Product(
          result[0],
          result[1],
          result[2],
          result[3],
          result[4],
          result[5],
          result[6],
          result[7],
          result[8],
          result[9],
      )

def create(
    conexao,
    id: int = None,
    fabricacao_timestamp: datetime = None,
    custo_unitario: float = None,
    nome: str = None,
    altura: float = None,
    comprimento: float = None,
    largura: float = None,
    massa: float = None,
    codigo_barra: str = None,
    estoque: int = None
):
    cursor = conexao.cursor()
    cursor.execute(
        "INSERT INTO Produto VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
        (
            id,
            fabricacao_timestamp,
            custo_unitario,
            nome,
            altura,
            comprimento,
            largura,
            massa,
            codigo_barra,
            estoque,
        ),
    )
    conexao.commit()

def delete_by_id(
    conexao,
    id: int = None,
):
    cursor = conexao.cursor()
    cursor.execute(
        "REMOVE Produto WHERE Id = (%s)",
        (
            id
        ),
    )
    conexao.commit()
