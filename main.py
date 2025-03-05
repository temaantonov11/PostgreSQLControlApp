from databaseAPI import *
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from coreGUI import interface

class DBClient:
    
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.StartWindow = interface.StartWindow()
        self.StartWindow.start_button.clicked.connect(self.login_button_clicked)
    
    def run(self):
        self.StartWindow.show()
        sys.exit(self.app.exec_())
        

    def login_button_clicked(self):

        username = self.StartWindow.username_field.text()
        password = self.StartWindow.password_field.text()

        if self.StartWindow.admin_option.isChecked():
            role = "Admin"
        else:
            role = "Guest"

        if self.StartWindow.login_option.isChecked():
            status = "LOGIN"
        else:
            status = "REGISTRY"

        self.db_client = DataBase()
        self.db_client.initUser(username, password, role, status)
        self.open_OpeninigDataBaseWindow()

    def open_OpeninigDataBaseWindow(self):
        self.openWindow = interface.OpeninigDataBaseWindow()
        self.openWindow.show()
        self.StartWindow.hide()

def main():
    client = DBClient()
    client.run()

if __name__ == "__main__":
    main()

