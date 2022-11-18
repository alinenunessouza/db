from fastapi import APIRouter

router = APIRouter()

@router.get("/products", tags=["products"])
async def read_users():
    return [
      {"name": "Celular",
       "description": "Legal"
      }
    ]