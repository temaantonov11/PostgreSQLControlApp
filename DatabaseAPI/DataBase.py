import psycopg2

from config import host, port, user, dbname, password

class DataBase:
    
    def __init__(self, username, role):
        self.username = username
        self.role = role
        self._connection = self._connect()

    def _create():
        pass
    
    def _connect(self):
        connection = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host,
            port=port
        )
        connection.autocommit = True
        return connection
