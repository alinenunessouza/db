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

def create(
    conexao,
    self,
    id: int = None,
    fabricacao_timestamp: datetime = None,
    custo_unitario: float = None,
    nome: str = None,
    altura: float = None,
    comprimento: float = None,
    largura: float = None,
    massa: float = None,
    codigo_barra: str = None,
    estoque: int = None,
):
    self._id = id
    self._fabricacao_timestamp = fabricacao_timestamp
    self._custo_unitario = custo_unitario
    self._nome = nome
    self._altura = altura
    self._comprimento = comprimento
    self._largura = largura
    self._massa = massa
    self._codigo_barra = codigo_barra
    self._estoque = estoque
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
