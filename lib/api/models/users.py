from .base_models import BaseModelWithUUID
from peewee import CharField


class Users(BaseModelWithUUID):
    discord_id = CharField(unique=True, max_length=50)
    name = CharField(unique=True, max_length=50)
