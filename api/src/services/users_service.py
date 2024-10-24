from ..schemas.users_schema import UserSchema
from ..models.users import Users


class UsersService:
    def __init__(self):
        pass

    async def register_user(user_data: UserSchema):
        # Check if user already exists
        existing_user = Users.get_or_none(Users.discord_id == user_data.discord_id)

        if existing_user:
            raise ValueError("User already registered")

        new_user = Users.create(**user_data.model_dump())
        return {"message": "User registerd successfully", "status_code": 201}
