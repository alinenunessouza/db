from fastapi import APIRouter
from app.services import orders

router = APIRouter()

@router.get("/orders", tags=["orders"])
async def get_all():
    return [
        {
            "id": "e80819a4-3e10-11ed-b878-0242ac120002",
            "status": "Criado",
            "timestamp": "'2022-08-25 11:35:04'",
            "id_comprador": "f6c48b12-3e10-11ed-b878-0242ac120002",
            "id_vendedor": "f23949ac-3e10-11ed-b878-0242ac120002",
        }
    ]

@router.get("/orders/{id}", tags=["orders"])
async def get_by_id(id: str):
    return {
        "status": "Criado",
        "timestamp": "'2022-08-25 11:35:04'",
        "id_comprador": "f6c48b12-3e10-11ed-b878-0242ac120002",
        "id_vendedor": "f23949ac-3e10-11ed-b878-0242ac120002",
    }

@router.post(
    "/orders/{id}/status",
    tags=["orders"],
    description="Atualiza o status de um pedido",
)
async def update_by_id_and_status(id:str, status: str):
    #adicionar validação para conforme o status ele for para uma tabela diferente
    orders.update_by_id_and_status(id,status)
    return {
        "Pedido atualizado com sucesso."
    }