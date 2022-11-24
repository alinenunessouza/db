from app.database import dependencies
from app.database.crud import user

cursor = dependencies.get_connection()


def get_all():
    return user.find_all(cursor)
