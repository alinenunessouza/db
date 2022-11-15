
from app.database.models.order import order

def find_all(self, cursor):
    cursor.execute("SELECT * FROM Pedido;")
    retorno = []
    for item in cursor.fetchall():
        retorno.append(order(item[0],item[1],item[2],item[3],item[4]))
    return retorno