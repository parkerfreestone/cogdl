from peewee import Field
from enum import Enum


class DivisionEnum(Enum):
    RAPTOR = "RAPTOR"
    KRUG = "KRUG"


class DivisionField(Field):
    def __init__(self, *args, **kwargs):
        self.choices = [division.value for division in DivisionEnum]
        super().__init__(*args, **kwargs)

    def db_value(self, value):
        if value not in self.choices:
            raise ValueError(
                f"Invalid division: {value}. Must be one of {self.choices}"
            )
        return value

    def python_value(self, value):
        return value
