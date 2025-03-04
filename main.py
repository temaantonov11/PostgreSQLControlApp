from databaseAPI import *

new_db = DataBase()

new_db.connect()

new_db.createDataBase("goods")

new_db.initUser("masik41111", "Admin", "123", "REGISTRY", "goods")



