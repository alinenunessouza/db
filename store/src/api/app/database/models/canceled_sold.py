'''Table Vendido_Cancelado '''

import datetime

class canceled_sold:

    def __init__(self, 
            quantidade:int=None,
            id_pedido:int=None,
            id_produto:int=None):
        self._quantidade = quantidade
        self._id_pedido = id_pedido
        self._id_produto = id_produto