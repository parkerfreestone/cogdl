from peewee import CharField, IntegerField, DateTimeField, UUIDField
from .base_models import BaseModelWithUUID

import datetime

class Teams(BaseModelWithUUID):
    name = CharField(unique=True, max_length=50)
    city = CharField(max_length=50)
    primary_color = CharField(max_length=7)
    secondary_color = CharField(max_length=7)
    stadium_name = CharField(max_length=50)
    
    # TODO: CHANGE THIS LATER WHEN DIVISIONS EXIST
    division = CharField
    
    wins = IntegerField(default=0)
    losses = IntegerField(default=0)

    created_at = DateTimeField(default=datetime.datetime.now)
    updated_at = DateTimeField(default=datetime.datetime.now)
