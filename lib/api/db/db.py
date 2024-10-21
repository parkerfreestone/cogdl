from ..models.base_models import database
from ..models.teams import Teams
from ..models.users import Users

def connect_database():
    database.connect()


def close_database():
    if not database.is_closed():
        database.close()


def create_tables(models):
    with database:
        database.create_tables(models)


def init_database():
    connect_database()
    create_tables([Teams, Users])