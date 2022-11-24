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

@router.put(
    "/products",
    tags=["products"],
    description="Adiciona um novo produto a listagem de produtos a venda no site",
)
async def add(custo_unitario: float, nome: str):
    """productService.Add(custo_unitario, nome, ...)"""
    return "Produto adicionado com sucesso"

@router.delete(
    "/products/{id}",
    tags=["products"],
    description="remove um produto do site buscando pelo id",
)
async def remove(id: str):
    """productService.Delete(id)"""
    return "Produto removido com sucesso"
