from databaseAPI import *
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox, QTableWidgetItem, QTableWidget
from queue import LifoQueue
from coreGUI import interface

class DBClient:
    
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.stack = LifoQueue()
        self.StartWindow = interface.StartWindow()
        self.OpenWindow = interface.OpeninigDataBaseWindow()
        self.ToolsWindow = interface.ToolsWindow()
        self.SearchWindow = interface.SearchWindow()
        self.SearchResultWindow = interface.SearchResultWindow()
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
        self.InsertWindow.back_button.clicked.connect(self.Back)
        self.InsertWindow.insert_button.clicked.connect(self.insert_button_clicked)
        self.SearchWindow.search_button.clicked.connect(self.search_button_clicked)
        self.SearchWindow.back_button.clicked.connect(self.Back)
        self.SearchResultWindow.back_button.clicked.connect(self.Back)
        self.UpdateWindow.back_button.clicked.connect(self.Back)
        self.UpdateWindow.update_button.clicked.connect(self.update_button_clicked)
        self.DeleteWindow.delete_button.clicked.connect(self.delete_button_clicked)
        self.DeleteWindow.back_button.clicked.connect(self.Back)

        
    
    def run(self):
        self.StartWindow.show()
        self.currentWindow = self.StartWindow
        self.stack.put(self.currentWindow)
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

    def Back(self):
        if self.stack.qsize() > 1:
            self.currentWindow.hide()
            self.stack.get()
            self.currentWindow = self.stack.queue[-1]
            self.currentWindow.show() 

    def insert_button_clicked(self):
        id = self.InsertWindow.id_field.text()
        brand = self.InsertWindow.brand_field.text()
        model = self.InsertWindow.model_field.text()
        year = self.InsertWindow.year_field.text()
        color = self.InsertWindow.color_field.text()

        self.db_client.insert(id, brand, model, year, color)

        self.InsertWindow.id_field.clear()
        self.InsertWindow.brand_field.clear()
        self.InsertWindow.model_field.clear()
        self.InsertWindow.year_field.clear()
        self.InsertWindow.color_field.clear()

    def search_button_clicked(self):
        brand = self.SearchWindow.nonkey_field.text()
        if not brand:
            QMessageBox.warning(self, "Field is empty.")
            return
        
        result = self.db_client.search(brand)

        self.SearchResultWindow.result_table.setRowCount(0)

        for row_number, row_data in enumerate(result):
            self.SearchResultWindow.result_table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.SearchResultWindow.result_table.setItem(row_number, column_number, QTableWidgetItem(str(data)))

        self.SearchWindow.nonkey_field.clear()
        self.Open(self.SearchResultWindow)
    
    def update_button_clicked(self):
        
        id = self.UpdateWindow.id_field.text()
        brand = self.UpdateWindow.brand_field.text()
        model = self.UpdateWindow.model_field.text()
        year = self.UpdateWindow.year_field.text()
        color = self.UpdateWindow.color_field.text()

        self.db_client.updateTable(id, brand, model, year, color)

        self.UpdateWindow.id_field.clear()
        self.UpdateWindow.brand_field.clear()
        self.UpdateWindow.model_field.clear()
        self.UpdateWindow.year_field.clear()
        self.UpdateWindow.color_field.clear()

    def delete_button_clicked(self):
        
        brand = self.DeleteWindow.delete_field.text()

        self.db_client.delete(brand)

        self.DeleteWindow.delete_field.clear()

    def SearchMenu_button_clicked(self):
        self.Open(self.SearchWindow)

    def DeleteMenu_button_clicked(self):
        self.Open(self.DeleteWindow)

    def UpdateMenu_button_clicked(self):
        self.Open(self.UpdateWindow)

    def ClearMenu_button_clicked(self):
        self.db_client.clearTable()

    def InsertMenu_button_clicked(self):
        self.Open(self.InsertWindow)
            

    def Open(self, Window):
        if self.currentWindow:
            self.currentWindow.hide()
        self.currentWindow = Window
        self.currentWindow.show()
        self.stack.put(self.currentWindow)

def main():
    client = DBClient()
    client.run()

if __name__ == "__main__":
    main()

