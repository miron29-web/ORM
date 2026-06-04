import sqlite3

from .abstact_database import DatabaseConnection
from ..settings import DATABASE_PATH

class SQLiteConnection(DatabaseConnection):
    db_path = DATABASE_PATH
    __connect = None

    @classmethod
    def connect(cls):
        if not cls.__connect:
            cls.__connect = sqlite3.connect(cls.db_path)
        return cls.__connect

    @classmethod
    def close(cls):
        if cls.__connect:
            cls.__connect.close()
            cls.__connect = None