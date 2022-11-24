from app.database.models.user import User

def find_all(cursor):
    cursor.execute("SELECT * FROM Usuario")
    result = []
    for item in cursor.fetchall():
        result.append(User(item[0], item[1], item[2], item[3], item[4]))
    return result

def create(
    conexao,
    cpf: str = None,
    nome: str = None,
    sobrenome: str = None,
    email: str = None,
    telefone: str = None,
):
    cursor = conexao.cursor()
    cursor.execute(
        "INSERT INTO Usuario VALUES(%s,%s,%s,%s,%s)",
        (cpf, nome, sobrenome, email, telefone),
    )
    conexao.commit()
