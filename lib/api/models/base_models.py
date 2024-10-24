from peewee import SqliteDatabase, Model, UUIDField, DateTimeField
import uuid
import datetime

DATABASE = "cogdl.db"

database = SqliteDatabase(DATABASE)


class BaseModel(Model):
    class Meta:
        database = database


class BaseModelWithUUID(BaseModel):
    id = UUIDField(primary_key=True, default=uuid.uuid4)

    created_at = DateTimeField(default=datetime.datetime.now)
    updated_at = DateTimeField(default=datetime.datetime.now)

    def save(self, *args, **kwargs):
        """Override the save method to automatically update the updated_at field."""
        self.updated_at = datetime.datetime.now()

        if not self.created_at:
            self.created_at = datetime.datetime.now()
        return super(BaseModelWithUUID, self).save(*args, **kwargs)
