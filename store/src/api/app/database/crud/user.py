
from app.database.models.user import user

def find_all(self, cursor):
    cursor.execute("SELECT * FROM Usuario;")
    retorno = []
    for item in cursor.fetchall():
        retorno.append(user(item[0],item[1],item[2],item[3],item[4]))
    return retorno