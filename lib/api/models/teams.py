from peewee import CharField, IntegerField, DateTimeField, UUIDField
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

    def dict(self):
        return {
            "id": str(self.id),
            "user": self.user,
            "name": self.name,
            "city": self.city,
            "primary_color": self.primary_color,
            "secondary_color": self.secondary_color,
            "stadium_name": self.stadium_name,
            "division": self.division,
            "wins": self.wins,
            "losses": self.losses,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }
