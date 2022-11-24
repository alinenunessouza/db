"""Table Comprador"""


class buyer:
    def __init__(self, id: int = None, cartao: str = None, cpf_usuario: str = None):
        self._id = id
        self._cartao = cartao
        self._cpf_usuario = cpf_usuario
