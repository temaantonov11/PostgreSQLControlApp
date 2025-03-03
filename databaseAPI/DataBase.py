import psycopg2
import psycopg2.sql
import logger
from .config import host, port, user, dbname, password

class DataBase:
     
    def __del__(self):
        self.__connection.close()
        logger.log.info("[POSTGRESQL]: Connection closed.")
    

    def createUser(self, username, role, passwd):
        try:
            self.__cursor.execute(psycopg2.sql.SQL("CREATE USER {} WITH PASSWORD %s;").format(psycopg2.sql.Identifier(username)), [passwd])
            self.__user = username
            self.__password = passwd
            self.__role = role
            logger.log.info(f"[POSTGRESQL]: User {self.__user} successfull created.")
        except psycopg2.Error as _ex:
            logger.log.error("[POSTGRESQL]: User did not create")
            
    
    def connect(self):
        try:
            self.__connection = psycopg2.connect(
                dbname=dbname,
                user=user,
                password=password,
                host=host,
                port=port
            )
            self.__connection.autocommit = True
            self.__cursor = self.__connection.cursor()
            logger.log.info("[POSTGRESQL]: Connection opened.")
        except psycopg2.Error as _ex:
            logger.log.error("[POSTGRESQL]: Connection error", _ex)
