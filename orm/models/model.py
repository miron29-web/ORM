from .model_meta import ModelMeta
from orm.db.db_manager import DatabaseManager
from ..fields import Field

class Model(DatabaseManager, metaclass=ModelMeta):

    def __init__(self, **kwargs):
        self.table_name = self.__class__.__name__.lower()

        for key, value in kwargs.items():
            setattr(self, key, value)

        super().__init__()

    def create_table(self):
        query_fields = list()

        for name, field in self._fields.items():
            query_fields.append(name + " " + field.get_query())

        sql = f"""CREATE TABLE IF NOT EXISTS `{self.table_name}` (
            {", ".join(query_fields)}
        );"""

        print(sql)
        self.execute(sql)

    def save(self):
        fields = list()
        values = list()

        for name in self._fields.keys():
            if not isinstance(getattr(self, name, None), Field):
                fields.append(name)
                values.append(getattr(self, name, None))

        sql = f"INSERT INTO {self.table_name} ({', '.join(fields)}) VALUES ({', '.join(['?']*len(values))})"

        self.execute(sql, tuple(values))