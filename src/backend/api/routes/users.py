from starlette.status import HTTP_201_CREATED
from fastapi import APIRouter, Depends, Body

from models.user import UserPublic, UserCreate
from api.dependencies.database import get_repository
from db.repositories.users import UsersRepository

router = APIRouter()


@router.post("/", response_model=UserPublic, name="users:register-new-user", status_code=HTTP_201_CREATED)
async def register_new_user(
    new_user: UserCreate = Body(..., embed=True),
    user_repo: UsersRepository = Depends(get_repository(UsersRepository))
) -> UserPublic:
    created_user = await user_repo.register_new_user(new_user=new_user)

    return created_user
