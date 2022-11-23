from app.database import dependencies
from app.database import crud

class product_service:

    def __init__(self):
        self._conexao = dependencies.get_connection

    def add(id:str, fabricacao_timestamp):
        crud.product.create(_conexao, id, fabricacao_timestamp)
