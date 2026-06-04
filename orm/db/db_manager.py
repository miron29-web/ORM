from .sqlite_database import SQLiteConnection

class DatabaseManager:
    def __init__(self):
        self.__db_connect = SQLiteConnection()

    def execute(self, sql):
        self.__db_connect.connect()
        cursor = self.__db_connect.cursor()
        cursor.close()
        self.__db_connect.close()