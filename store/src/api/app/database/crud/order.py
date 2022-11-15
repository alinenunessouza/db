
from app.database.models.order import order

def find_all(self, cursor):
    cursor.execute("SELECT * FROM Pedido;")
    retorno = []
    for item in cursor.fetchall():
        retorno.append(order(item[0],item[1],item[2],item[3],item[4]))
    return retorno

def find_by_id(self, cursor, id):
    cursor.execute("SELECT * FROM Pedido WHERE id = '{id}';")
    retorno = []
    for item in cursor.fetchall():
        retorno.append(order(item[0],item[1],item[2],item[3],item[4]))
    return retorno

def update_by_id(self, cursor, conexao, id, status):
    cursor.execute("UPDATE Pedido set status = '{status}' WHERE id = '{id}';")
    conexao.commit()