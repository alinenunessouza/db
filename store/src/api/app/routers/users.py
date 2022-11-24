from fastapi import APIRouter, Request
from app.services import user
from pydantic import BaseModel

router = APIRouter()

class UserDTO(BaseModel):
  cpf: str
  nome: str
  sobrenome: str
  email: str
  telefone: str

@router.get("/users", tags=["users"])
async def get_all():
    return user.get_all()

@router.post("/users", tags=["users"])
async def create(request: UserDTO):
    return request.json()

# @router.put(
#     "/users", tags=["users"], description="Criar um novo perfil de usuário no site."
# )
# async def create(cpf: str, nome: str, sobrenome: str, email: str, telefone: str):
#     """userService.Add(cpf, nome, ...)"""
#     return "Cadastro realizado com sucesso!"
