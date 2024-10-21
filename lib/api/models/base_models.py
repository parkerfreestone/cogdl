from peewee import SqliteDatabase, Model, UUIDField
import uuid

DATABASE = 'cogdl.db'

database = SqliteDatabase(DATABASE)

class BaseModel(Model):
    class Meta:
        database = database


class BaseModelWithUUID(BaseModel):
    id = UUIDField(primary_key=True, default=uuid.uuid4)