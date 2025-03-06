import psycopg2
import psycopg2.sql
from logger import *
from .config import host, port, user, dbname, password
from .procedures import *

class PostgreSQLManager:
     
    def __init__(self, user=user, passwd=password):
        self.__user = user
        self.__password = passwd
    
    def __del__(self):
        
        if self.__connection != None:
            self.disconnect()
    

    def initUser(self, username, role, passwd, status):
        try:
            if status == "REGISTRY":
                self.connect(dbname)
                self.__createUser(username, role, passwd)
                self.__setRole(username, role)
                self.disconnect()
            if status == "LOGIN":
                self.__user = username
                self.__password = passwd
                self.__role = role
                log.info(f"Log in successfuly: {self.__user}, {self.__role}")
            self.__connection = None
            
        except psycopg2.Error as _ex:
            log.error("[POSTGRESQL]: User did not init", _ex)
            

    def __createUser(self, username, role, passw):
        try:
            self.__cursor.execute(psycopg2.sql.SQL("CREATE USER {} WITH PASSWORD %s;").format(psycopg2.sql.Identifier(username)), [passw])
            self.__user = username
            self.__password = passw
            self.__role = role
            log.info(f"[POSTGRESQL]: User {username} successfull created.")
        except psycopg2.Error as _ex:
            log.error("[POSTGRESQL]: User did not create", _ex)

    def __setRole(self, user, role):
        
        try:
            if (role == "Admin"):
                self.__cursor.execute(psycopg2.sql.SQL("GRANT ALL PRIVILEGES ON DATABASE {} TO {};").format(psycopg2.sql.Identifier(dbname), psycopg2.sql.Identifier(user)))
                self.__cursor.execute(psycopg2.sql.SQL("GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO {};").format(psycopg2.sql.Identifier(user)))
                self.__cursor.execute(psycopg2.sql.SQL("ALTER ROLE {} CREATEDB;").format(psycopg2.sql.Identifier(user)))
                log.info(f"[POSTGRESQL]: {user} became admin")
            elif (role == "Guest"):
                self.__cursor.execute(psycopg2.sql.SQL("GRANT USAGE ON SCHEMA public TO {};").format(psycopg2.sql.Identifier(user)))
                self.__cursor.execute(psycopg2.sql.SQL("GRANT SELECT ON ALL TABLES IN SCHEMA public TO {};").format(psycopg2.sql.Identifier(user)))
                log.info(f"[POSTGRESQL]: {user} became guest")
        except psycopg2.Error as _ex:
            log.error("[POSTGRESQL]: Error when granting admin/guest rights", _ex)

    def createDataBase(self, newDbName):
        try:
            self.connect()
            self.__cursor.execute(psycopg2.sql.SQL("CREATE DATABASE {};").format(psycopg2.sql.Identifier(newDbName)))
            self.disconnect()
            self.connect(newDbName)
            log.info(f"[POSTGRESQL]: DB {newDbName} created.")
            self.__createTable()
        except psycopg2.Error as _ex:
            log.error(f"[POSTGRESQL]: Failed create {newDbName} DB.\n {_ex}")

    def dropDatabase(self, db):
        
        try:
            self.connect(dbname)
            self.__cursor.execute(psycopg2.sql.SQL("ALTER DATABASE {} CONNECTION LIMIT 0;").format(psycopg2.sql.Identifier(db)))
            self.__cursor.execute(psycopg2.sql.SQL("DROP DATABASE IF EXISTS {};").format(psycopg2.sql.Identifier(db)))
            log.info(f"[POSTGRESQL]: database {db} dropped.")
        except psycopg2.Error as _ex:
            log.error(f"[POSTGRESQL]: Failed drop database {db}. \n {_ex}")



    def __createTable(self):
        try:
            self.__cursor.execute(create_table_sql)
            log.info("[POSTGRESQL]: Table created. ")
        except psycopg2.Error as _ex:
            log.error(f"[POSTGRESQL]: Failed create table. \n {_ex}")
    
    def insert(self, id, brand, model, year, color):
        try:
            self.__cursor.execute(insert_sql)
            self.__cursor.callproc("insert_car", (id, brand, model, year, color))
            log.info("[POSTGRESQL]: sucessfull insert")
        except psycopg2.Error as _ex:
            log.error(f"[POSTGRESQL]: Failed insert. \n {_ex}")

    def clearTable(self):
        try:
            self.__cursor.execute(clear_table_sql)
            self.__cursor.callproc("clear_table")
            log.info("[POSTGRESQL]: Successful clear table.")

        except psycopg2.Error as _ex:
            log.error(f"[POSTGRESQL]: Failed clear table. \n {_ex}")
    
    def search(self, brand):
        try:
            self.__cursor.execute(search_by_brand)
            self.__cursor.callproc("search", (brand, ))
            result = self.__cursor.fetchall()
            log.info("[POSTGRESQL]: Successful search.")
            return result
        except psycopg2.Error as _ex:
            log.error(f"[POSTGRESQL]: Failed search.\n {_ex}")
            return None
    
    def selectAll(self):
        try:
            self.__cursor.execute(selectall_sql)
            self.__cursor.callproc("select_sql")
            result = self.__cursor.fetchall()
            log.info("[POSTGRESQL]: Successful select.")
            return result
        except psycopg2.Error as _ex:
            log.error(f"[POSTGRESQL]: Select failed. \n {_ex}")
            return None

    def updateTable(self, id, brand, model, year, color):
        try:
            self.__cursor.execute(update_sql)
            self.__cursor.callproc("update_tuple", (id, brand, model, year, color))
            log.info("[POSTGRESQL]: Successful update table.")
        except psycopg2.Error as _ex:
            log.error(f"[POSTGRESQL]: Failed update table. \n {_ex}")

    def delete(self, brand):
        try:
            self.__cursor.execute(delete_sql)
            self.__cursor.callproc("delete_sql", (brand, ))
            log.info("[POSTGRESQL]: Successful delete tuples.")
        except psycopg2.Error as _ex:
            log.error(f"[POSTGRESQL]: Failed delete tuples. \n {_ex}")

    def connect(self, db = dbname):
        try:
            self.__connection = psycopg2.connect(
                dbname=db,
                user=self.__user,
                password=self.__password,
                host=host,
                port=port
            )
            self.__connection.autocommit = True
            self.__cursor = self.__connection.cursor()
            log.info(f"[POSTGRESQL]: {self.__user} connected to {db}.")
        except psycopg2.Error as _ex:
            log.error("[POSTGRESQL]: Connection error {}".format(_ex))

    def disconnect(self):
        try:
            self.__connection.close()
            self.__cursor.close()
            self.__connection = None
            log.info(f"[POSTGRESQL]: {self.__user} disconnected.")
        except psycopg2.Error as _ex:
            log.error("[POSTGRESQL]: disconnection error")