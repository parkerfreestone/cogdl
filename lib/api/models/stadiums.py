from peewee import CharField, IntegerField
from .base_models import BaseModelWithUUID
import random


class Stadiums(BaseModelWithUUID):
    name = CharField(max_length=50)
    state = CharField(max_length=50)
    city = CharField(max_length=50)
    capacity = IntegerField(default=lambda: random.randint(80000, 110000))
