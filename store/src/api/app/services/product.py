from app.database import dependencies
from app.database import crud

class product_service:

    def __init__(self):
        self.conn = dependencies.get_connection

    def add(self, id: str, fabricacao_timestamp):
        crud.product.create(conn, id, fabricacao_timestamp)
