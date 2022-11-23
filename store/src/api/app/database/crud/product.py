
from app.database.models.product import product
import datetime

def create(conexao,
            self,
            id:int=None, 
            fabricacao_timestamp:datetime=None,
            custo_unitario:float = None,
            nome:str = None,
            altura:float = None,
            comprimento:float = None,
            largura:float = None,
            massa:float = None,
            codigo_barra:str = None,
            estoque:int=None):
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
        cursor.execute("INSERT INTO Produto VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
            (id,
            fabricacao_timestamp,
            custo_unitario,
            nome,
            altura,
            comprimento,
            largura,
            massa,
            codigo_barra,
            estoque));
        conexao.commit()