from fastapi import APIRouter

router = APIRouter()

@router.get("/users/", tags=["users"])
async def get_all():
    return [{"username": "Rick"}, {"username": "Morty"}]


@router.get("/users/me", tags=["users"])
async def read_user_me():
    return {"username": "fakecurrentuser"}


@router.get("/users/{name}", tags=["users"])
async def get_by_name(name: str):
    return {"nome": name}