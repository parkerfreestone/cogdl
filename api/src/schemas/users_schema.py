from pydantic import BaseModel


class UserSchema(BaseModel):
    discord_id: str
    name: str
