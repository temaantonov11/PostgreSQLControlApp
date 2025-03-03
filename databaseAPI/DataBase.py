import psycopg2
import logger
from .config import host, port, user, dbname, password

class DataBase:
    
    def __init__(self, username, role):
        self.__username = username
        self.__role = role
        self.__connection = self.__connect()
    
    def __del__(self):
        self.__connection.close()
        logger.log.info("[POSTGRESQL]: Connection closed.")
        

    def _create():
        pass
    
    def __connect(self):
        try:
            connection = psycopg2.connect(
                dbname=dbname,
                user=user,
                password=password,
                host=host,
                port=port
            )
            connection.autocommit = True
            logger.log.info("[POSTGRESQL]: Connection opened.")
            return connection
        except Exception as _ex:
            logger.log.error("[POSTGRESQL]: Connection error", _ex)
