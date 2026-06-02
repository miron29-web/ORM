class DatabaseManager:
    def __init__(self, db_connect):
        self.__db_connect = db_connect

    def execute(self, sql):
        self.__db_connect.connect()
        cursor = self.__db_connect.cursor()

        cursor.close()
        self.__db_connect.close()