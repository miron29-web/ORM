from .model_meta import ModelMeta
from orm.db.db_manager import DatabaseManager

class Model(DatabaseManager, metaclass=ModelMeta):
    def __init__(self, **kwargs):
        self._table_name = self.__class__.__name__.lower()

        for key, value in kwargs.items():
            setattr(self, key, value)

    def create_table(self):
        fields = []
        values = []

        for name, field in self._fields.items():
            print(name, field)