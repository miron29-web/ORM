from .model_meta import ModelMeta
from orm.db.db_manager import DatabaseManager

class Model(DatabaseManager, metaclass=ModelMeta):
    def __init__(self, **kwargs):
        self._table_name = self.__class__.__name__.lower()

        for key, value in kwargs.items():
            setattr(self, key, value)

        super().__init__()

    def create_table(self):
        query_fields = list()

        for name, field in self._fields.items():
            query_fields.append(name + " " + field.get_query())

        sql = f"""CREATE TABLE IF NOT EXISTS `{self._table_name}` (
            {", ".join(query_fields)}
        );"""

        print(sql)
        self.execute(sql)