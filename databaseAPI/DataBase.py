import psycopg2
import psycopg2.sql
from logger import *
from .config import host, port, user, dbname, password



class DataBase:
     
    def __del__(self):
        self.__connection.close()
        log.info("[POSTGRESQL]: Connection closed.")
    
    
    def initUser(self, username, role, passwd):
        try:
            self.__createUser(username, role, passwd)
            self.__setRole(username, role)
            self.__user = username
            self.__password = passwd
            self.__role = role
        except psycopg2.Error as _ex:
            log.error("[POSTGRESQL]: User did not init", _ex)
            

    def __createUser(self, username, role, passw):
        try:
            self.__cursor.execute(psycopg2.sql.SQL("CREATE USER {} WITH PASSWORD %s;").format(psycopg2.sql.Identifier(username)), [passw])
            log.info(f"[POSTGRESQL]: User {username} successfull created.")
        except psycopg2.Error as _ex:
            log.error("[POSTGRESQL]: User did not create", _ex)

    def __setRole(self, user, role):
        
        try:
            if (role == "Admin"):
                self.__cursor.execute(psycopg2.sql.SQL("GRANT ALL PRIVILEGES ON DATABASE {} TO {};").format(psycopg2.sql.Identifier(dbname), psycopg2.sql.Identifier(user)))
                self.__cursor.execute(psycopg2.sql.SQL("GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO {};").format(psycopg2.sql.Identifier(user)))
                log.info(f"[POSTGRESQL]: {user} became admin")
            elif (role == "Guest"):
                self.__cursor.execute(psycopg2.sql.SQL("GRANT USAGE ON SCHEMA public TO {};").format(psycopg2.sql.Identifier(user)))
                self.__cursor.execute(psycopg2.sql.SQL("GRANT SELECT ON ALL TABLES IN SCHEMA public TO {};").format(psycopg2.sql.Identifier(user)))
                log.info(f"[POSTGRESQL]: {user} became guest")
        except psycopg2.Error as _ex:
            log.error("[POSTGRESQL]: Error when granting admin/guest rights", _ex)

    
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
            log.info("[POSTGRESQL]: Connection opened.")
        except psycopg2.Error as _ex:
            log.error("[POSTGRESQL]: Connection error", _ex)
