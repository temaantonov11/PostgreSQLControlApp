from databaseAPI import *
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from coreGUI import interface

class DBClient:
    
    def __init__(self):
        self.app = QApplication(sys.argv)

        self.StartWindow = interface.StartWindow()
        self.OpenWindow = interface.OpeninigDataBaseWindow()
        self.ToolsWindow = interface.ToolsWindow()
        self.SeachWindow = interface.SearchWindow()
        self.DeleteWindow = interface.DeleteWindow()
        self.ClearWindow = interface.ClearWindow()
        self.InsertWindow = interface.InsertWindow()
        self.UpdateWindow = interface.UpdateWindow()

        self.StartWindow.start_button.clicked.connect(self.login_button_clicked)
        self.OpenWindow.start_button.clicked.connect(self.openDB_button_clicked)
        self.ToolsWindow.searchButton.clicked.connect(self.SearchMenu_button_clicked)
        self.ToolsWindow.deleteButton.clicked.connect(self.DeleteMenu_button_clicked)
        self.ToolsWindow.clearButton.clicked.connect(self.ClearMenu_button_clicked)
        self.ToolsWindow.updateButton.clicked.connect(self.UpdateMenu_button_clicked)
        self.ToolsWindow.insertButton.clicked.connect(self.InsertMenu_button_clicked)

        
    
    def run(self):
        self.StartWindow.show()
        self.currentWindow = self.StartWindow
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
        self.db_client.initUser(username, role, password, status)
        self.Open(self.OpenWindow)
    
    def openDB_button_clicked(self):
        
        nameDB = self.OpenWindow.nameDB_field.text()

        if self.OpenWindow.openDB_radio.isChecked():
            self.db_client.connect(nameDB)
        else:
            self.db_client.createDataBase(nameDB)

        self.Open(self.ToolsWindow)

    def SearchMenu_button_clicked(self):
        self.Open(self.SeachWindow)

    def DeleteMenu_button_clicked(self):
        self.Open(self.DeleteWindow)

    def UpdateMenu_button_clicked(self):
        self.Open(self.UpdateWindow)

    def ClearMenu_button_clicked(self):
        self.Open(self.ClearWindow)

    def InsertMenu_button_clicked(self):
        self.Open(self.UpdateWindow)
            

    def Open(self, Window):
        Window.show()
        self.currentWindow.hide()
        self.previousWindow = self.currentWindow
        self.currentWindow = Window        

def main():
    client = DBClient()
    client.run()

if __name__ == "__main__":
    main()

