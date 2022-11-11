class ProdutoDb:

    def __init__(self, id, fabricacao_timestamp, custo_unitario, nome, altura, comprimento, largura, massa, codigo_barra, estoque):
        self.id = id
        self.fabricacao_timestamp = fabricacao_timestamp
        self.custo_unitario = custo_unitario
        self.nome = nome
        self.altura = altura
        self.comprimento = comprimento
        self.largura = largura
        self.massa = massa
        self.codigo_barra = codigo_barra
        self.estoque = estoque

    @classmethod
    def adicionar(cls, item):
        cls.items.append(item)
        return True
    @classmethod
    def obter(cls, id=None):
        if id:
            return next(filter(lambda x: x['id'] == id,cls.items),{})
        return cls.items
    @classmethod
    def remover(cls, id):
        cls.items = list(filter(lambda x: x['id'] != id, cls.items))
        return {"mensagem": f"id {id} deletado com sucesso"}
    @classmethod
    def alterar(cls, id, novo_item:dict):
        item = next(filter(lambda x: x['id'] == id,cls.items),{})
        index = cls.items.index(item)

        if novo_item.get('nome'):
            item['nome'] = novo_item.get('nome')

        if novo_item.get('endereco'):
            item['endereco'] = novo_item.get('endereco')

        cls.items[index] = item
        return item