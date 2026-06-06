from .sqlite_database import SQLiteConnection

class DatabaseManager:
    def __init__(self):
        self.__db_connect = SQLiteConnection()

    def execute(self, sql, values=None):
        connect = self.__db_connect.connect()
        cursor = connect.cursor()
        if values:
            cursor.execute(sql, values)
        else:
            cursor.execute(sql)

        self.__db_connect.commit()
        self.__db_connect.close()