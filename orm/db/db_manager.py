from .sqlite_database import SQLiteConnection

class DatabaseManager:
    def __init__(self):
        self.__db_connect = SQLiteConnection()

    def execute(self, sql):
        connect = self.__db_connect.connect()
        cursor = connect.cursor()

        cursor.execute(sql)

        cursor.close()
        self.__db_connect.close()