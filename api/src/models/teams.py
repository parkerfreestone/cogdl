from peewee import CharField, ForeignKeyField
from ..db.fields.division_field import DivisionField
from .base_models import BaseModelWithUUID
from .stadiums import Stadiums
from .users import Users


class Teams(BaseModelWithUUID):
    # Discord user associated with the team
    user = ForeignKeyField(Users, backref="team")

    # Team Display items
    name = CharField(unique=True, max_length=50)
    city = CharField(max_length=50)
    primary_color = CharField(max_length=7)
    secondary_color = CharField(max_length=7)

    # Custom division field to restrict entries
    division = DivisionField(null=True)

    stadium = ForeignKeyField(Stadiums, backref="team")
