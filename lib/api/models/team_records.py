from peewee import ForeignKeyField, IntegerField
from .base_models import BaseModelWithUUID
from .teams import Teams
from .seasons import Seasons


class TeamRecords(BaseModelWithUUID):
    team = ForeignKeyField(Teams, backref="records")
    season = ForeignKeyField(Seasons, backref="team_records")
    wins = IntegerField(default=0)
    losses = IntegerField(default=0)
