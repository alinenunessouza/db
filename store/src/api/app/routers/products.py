from fastapi import APIRouter

router = APIRouter()

@router.get("/products", tags=["products"], description='Lista todos os produtos disponíveis no site')
async def get_all():
    return [
          {
            "id": '9c0fa044-3e10-11ed-b878-0242ac120002',
            "fabricacao_timestamp": '2022-06-25 10:00:00',
            "custo_unitario": 4149.00,
            "nome": 'Geladeira Panasonic Frost Free 483L A+++',
            "altura": 155,
            "comprimento": 65,
            "largura": 60,
            "massa": 73,
            "codigo_barra": 8980907523,
            "estoque": 40
      }
    ]

@router.put("/products", tags=["products"], description='Adiciona um novo produto a listagem de produtos a venda no site')
async def add(custo_unitario:float, nome:str):
    '''productService.Add(custo_unitario, nome, ...)'''
    return "Produto adicionado com sucesso"

'''remove um produto do site'''
@router.delete("/products/{id}", tags=["products"])
async def add(id:str):
    '''productService.Delete(id)'''
    return "Produto removido com sucesso"
