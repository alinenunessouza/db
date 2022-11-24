from fastapi import APIRouter, Depends
from app.services import user

router = APIRouter()

@router.get("/users", tags=["users"])
async def get_all():
    return user.get_all()

@router.get("/users/me", tags=["users"])
async def read_user_me():
    return {"username": "fakecurrentuser"}


@router.get("/users/{name}", tags=["users"])
async def get_by_name(name: str):
    return {"nome": name}

@router.put("/users", tags=["users"], description='Criar um novo perfil de usuário no site.')
async def create(cpf:str, nome:str, sobrenome:str, email:str, telefone:str):
    '''userService.Add(cpf, nome, ...)'''
    return "Cadastro realizado com sucesso!"