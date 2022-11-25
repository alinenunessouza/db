from app.database import dependencies
from app.database.crud import order

cursor = dependencies.get_connection()

def get_all():
    return order.find_all(cursor)

def find_by_id(id:str):
    return order.find_by_id(cursor, id)

def create(cpf:str, id_products:str):
    return order.create(cursor, cpf, id_products)

def update_by_id_and_status(id:str, status:str):
    return order.update_by_id(cursor, id, status)
