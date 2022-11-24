from fastapi import APIRouter

router = APIRouter()

@router.put(
    "/cart",
    tags=["cart"],
    description="Adiciona um produto no carrinho pelo id que está armazenado no banco.",
)
async def add(id: str):
    return "Produto adicionado ao carrinho com sucesso!"

@router.put(
    "/cart/new_order",
    tags=["cart"],
    description="Realiza um novo pedido com os produtos que estão no carrinho do usuário.",
)
async def add(id: str):
    "pega o id usuario pelo login"
    return "Pedido realizado com sucesso!"
