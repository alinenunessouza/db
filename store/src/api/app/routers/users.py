from fastapi import APIRouter, Request
from app.services import user

router = APIRouter()

@router.get("/users", tags=["users"])
async def get_all():
    return user.get_all()

@router.post("/users", tags=["users"], description="Criar um novo perfil de usuário no site.")
async def create(request: user.UserDTO):
    user.create(request)
    return request.json()

# @router.put(
#     "/users", tags=["users"], description="Criar um novo perfil de usuário no site."
# )
# async def create(cpf: str, nome: str, sobrenome: str, email: str, telefone: str):
#     """userService.Add(cpf, nome, ...)"""
#     return "Cadastro realizado com sucesso!"
