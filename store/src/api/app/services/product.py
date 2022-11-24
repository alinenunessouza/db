from app.database import dependencies
from app.database.crud import product

cursor = dependencies.get_connection()


def get_all():
    return product.find_all(cursor)
