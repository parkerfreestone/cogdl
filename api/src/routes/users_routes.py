from fastapi import APIRouter, HTTPException, status
from ..schemas.users_schema import UserSchema
from ..services.users_service import UsersService

# Route Config
users_router = APIRouter(prefix="/users", tags=["users"])


@users_router.post("/", status_code=status.HTTP_201_CREATED)
async def register_user(user_data: UserSchema):
    try:
        result = await UsersService.register_user(user_data)
        return result
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
