from peewee import CharField, DateTimeField
from .base_models import BaseModelWithUUID


class Seasons(BaseModelWithUUID):
    name = CharField(max_length=50)
    start_date = DateTimeField(null=True)
    end_date = DateTimeField(null=True)
