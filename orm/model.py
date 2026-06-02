from orm.db.db_manager import DatabaseManager
from .base_model import BaseModel
from fields import Field, CharField

class Model(BaseModel ,DatabaseManager):
    def __init__(self):
        self.__table_name = self.__class__.__name__.lower()
        super().__init__()

    @classmethod
    def __get_fields(cls):
        return [
            value for value in cls.__dict__.values()
            if isinstance(value, Field)
        ]

    def create_table(self):
        fields = self.__get_fields()
