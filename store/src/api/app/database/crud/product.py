from app.database.models.product import Product
import datetime

def find_all(cursor):
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

def find_by_id(cursor, id:str):
    cursor.execute("SELECT * FROM Produto WHERE Id = {id}")
    for item in cursor.fetchall():
        return Product(
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
    return None

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
