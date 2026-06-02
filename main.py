from orm.db.sqlite_database import SQLiteConnection

def main():
    sql = SQLiteConnection()
    sql.connect()
if __name__ == '__main__':
    main()