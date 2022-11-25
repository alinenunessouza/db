from app.database.models.order import Order

def find_all(cursor):
    cursor.execute("SELECT * FROM Pedido;")
    retorno = []
    for item in cursor.fetchall():
        retorno.append(Order(item[0], item[1], item[2], item[3], item[4]))
    return retorno

def find_by_id(cursor, id):
    cursor.execute("SELECT * FROM Pedido WHERE id = '" + id + "';")
    for item in cursor.fetchall():
        return Order(item[0], item[1], item[2], item[3], item[4])
    return None

def create(conexao, id, id_products):
    cursor = conexao.cursor()
    cursor.execute(
        "INSERT INTO Pedido VALUES(%s,%s,%s,%s,%s)",
        (
        id,
        status,
        timestamp,
        id_comprador,
        id_vendedor
        ) 
    )
    conexao.commit()
    return "Pedido realizado com sucesso"

def update_by_id(conexao, id, status):
    cursor = conexao.cursor()
    cursor.execute(
        "UPDATE Pedido set status = '" + status + "' WHERE id = '" + id + "';"
    )
    conexao.commit()
