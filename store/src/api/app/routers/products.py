from fastapi import APIRouter
from app.services import product

router = APIRouter()

@router.get(
    "/products",
    tags=["products"],
    description="Lista todos os produtos disponíveis no site",
)
async def get_all():
    return product.get_all()

@router.get(
    "/products/{id}",
    tags=["products"],
    description="Busca o produto do site correspondente ao identificador informado.",
)
async def get_by_id(id: str):
    return product.get_by_id(id)

@router.post(
    "/products", tags=["products"], description="Adiciona um novo produto a listagem de produtos a venda no site."
)
async def create(request: product.CreateProductDTO):
    product.create(request)
    return request.json()



# @router.put(
#     "/products",
#     tags=["products"],
#     description="Adiciona um novo produto a listagem de produtos a venda no site",
# )
# async def add(request: product.ProductDTO):
#     product.create(request)
#     return "Produto adicionado com sucesso"

# @router.delete(
#     "/products/{id}",
#     tags=["products"],
#     description="remove um produto do site buscando pelo id",
# )
# async def remove(id: str):
#     product.delete(id)
#     return "Produto removido com sucesso"
