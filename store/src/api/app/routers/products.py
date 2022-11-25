from fastapi import APIRouter
from app.services import products

router = APIRouter()

@router.get(
    "/products",
    tags=["products"],
    description="Lista todos os produtos disponíveis no site",
)
async def get_all():
    return products.get_all()

@router.get(
    "/products/{id}",
    tags=["products"],
    description="Busca o produto do site correspondente ao identificador informado.",
)
async def get_by_id(id: str):
    return products.get_by_id(id)

@router.put(
    "/products",
    tags=["products"],
    description="Adiciona um novo produto a listagem de produtos a venda no site",
)
async def add(request: products.ProductDTO):
    products.create(request)
    return "Produto adicionado com sucesso"

@router.delete(
    "/products/{id}",
    tags=["products"],
    description="remove um produto do site buscando pelo id",
)
async def remove(id: str):
    products.delete(id)
    return "Produto removido com sucesso"
