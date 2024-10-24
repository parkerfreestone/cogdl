from peewee import CharField, IntegerField, DateTimeField
from .base_models import BaseModelWithUUID

import datetime

class Teams(BaseModelWithUUID):
    # Discord user associated with the team
    user = CharField(unique=True, max_length=50, null=True)

    name = CharField(unique=True, max_length=50)
    city = CharField(max_length=50)
    primary_color = CharField(max_length=7)
    secondary_color = CharField(max_length=7)
    stadium_name = CharField(max_length=50)
    
    # TODO: Change this later when divisions exist
    division = CharField(max_length=50, null=True)
    
    # TODO: More R&D on this... Might have a seperate table for specific games/records
    wins = IntegerField(default=0)
    losses = IntegerField(default=0)

    created_at = DateTimeField(default=datetime.datetime.now)
    updated_at = DateTimeField(default=datetime.datetime.now)
