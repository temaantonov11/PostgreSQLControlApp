from databaseAPI import *

new_db = DataBase()




new_db.initUser("serega1", "Admin", "123", "REGISTRY")
new_db.createDataBase("boomers")
new_db.connect("boomers")


