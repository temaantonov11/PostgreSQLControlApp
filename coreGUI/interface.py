import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel,
                             QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QPushButton,
                             QCheckBox, QRadioButton, QButtonGroup, QLineEdit, QTableWidget)
from PyQt5.QtCore import Qt

class StartWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        
        self.setWindowTitle("carDB")
        self.setGeometry(500, 200, 800, 500)
        
        central_widget = QWidget()
        
        self.setCentralWidget(central_widget)
       
        main_layout = QVBoxLayout(central_widget)

        
        central_widget.setStyleSheet("""
            QWidget {
                padding: 0px;
                margin: 0px;
            }
            QLabel {
                padding: 0px;
                margin: 0px;
                font-size: 15px;
            }
            QLineEdit {
                font-size: 16px;
                padding: 5px;
                margin: 0px;
            }
        """)

        info_title = QLabel("Input user data and choose role")
        info_title.setStyleSheet("font-size: 20px;")

        self.username_field = QLineEdit(self)
        self.password_field = QLineEdit(self)

        self.admin_option = QRadioButton("Admin")
        self.guest_option = QRadioButton("Guest")

        self.login_option = QRadioButton("log in")
        self.registry_option = QRadioButton("sign up")

        self.start_button = QPushButton("Start")

        self.role_group = QButtonGroup()
        self.role_group.addButton(self.admin_option, 1)
        self.role_group.addButton(self.guest_option, 2)

        self.init_group = QButtonGroup()
        self.init_group.addButton(self.login_option, 1)
        self.init_group.addButton(self.registry_option, 2)

        info_layout = QHBoxLayout()
        
        role_layout = QHBoxLayout()
        role_layout.setSpacing(0)
        role_layout.setContentsMargins(0, 0, 0, 0)

        auth_layout = QVBoxLayout()
        auth_layout.setSpacing(0)
        auth_layout.setContentsMargins(0, 0, 0, 0)

        init_layout = QHBoxLayout()
        init_layout.setSpacing(0)
        init_layout.setContentsMargins(0, 0, 0, 0)

        info_layout.addWidget(info_title)

        auth_layout.addWidget(QLabel('Username: '))
        auth_layout.addWidget(self.username_field)
        auth_layout.addWidget(QLabel('Password: '))
        auth_layout.addWidget(self.password_field)

        role_layout.addWidget(self.admin_option)
        role_layout.addWidget(self.guest_option)        
        
        init_layout.addWidget(self.login_option)
        init_layout.addWidget(self.registry_option)

        main_layout.addLayout(info_layout)
        main_layout.addLayout(auth_layout)
        main_layout.addLayout(role_layout)
        main_layout.addLayout(init_layout)
        main_layout.addWidget(self.start_button)

        info_layout.addStretch(1)
        auth_layout.addStretch(1)
        role_layout.addStretch(1)
        init_layout.addStretch(1)
        main_layout.addStretch(1)
        
        
class OpeninigDataBaseWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setWindowTitle("carDB")
        self.setGeometry(500, 200, 800, 500)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        main_layout = QVBoxLayout(central_widget)

        self.nameDB_field = QLineEdit()

        self.openDB_radio = QRadioButton("Open DB")
        self.createDB_radio = QRadioButton("Create DB")

        self.start_button = QPushButton("Open DB")

        self.actionDB_group = QButtonGroup()
        self.actionDB_group.addButton(self.openDB_radio)
        self.actionDB_group.addButton(self.createDB_radio)

        field_layout = QHBoxLayout()
        field_layout.setSpacing(0)
        field_layout.setContentsMargins(0, 0, 0, 0)

        radioButtons_layout = QHBoxLayout()
        radioButtons_layout.setSpacing(0)
        radioButtons_layout.setContentsMargins(0, 0, 0, 0)

        field_layout.addWidget(QLabel('Database name: '))
        field_layout.addWidget(self.nameDB_field)

        radioButtons_layout.addWidget(self.openDB_radio)
        radioButtons_layout.addWidget(self.createDB_radio)

        main_layout.addLayout(field_layout)
        main_layout.addLayout(radioButtons_layout)
        main_layout.addWidget(self.start_button)

        field_layout.addStretch(1)
        radioButtons_layout.addStretch(1)
        main_layout.addStretch(1)

class ToolsWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.setupUI()
    
    def setupUI(self):
        
        self.setWindowTitle("carDB")
        self.setGeometry(500, 200, 800, 500)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        main_layout = QGridLayout(central_widget)

        self.searchButton = QPushButton("Search")
        self.deleteButton = QPushButton("Delete")
        self.clearButton = QPushButton("Clear DB")
        self.updateButton = QPushButton("Update")
        self.insertButton = QPushButton("Insert")

        main_layout.addWidget(self.searchButton, 0, 0)
        main_layout.addWidget(self.deleteButton, 0, 1)
        main_layout.addWidget(self.clearButton, 1, 0)
        main_layout.addWidget(self.updateButton, 1, 1)
        main_layout.addWidget(self.insertButton, 2, 0)

class SearchWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setWindowTitle("carDB")
        self.setGeometry(500, 200, 800, 500)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        main_layout = QVBoxLayout(central_widget)

        self.nonkey_field = QLineEdit()

        self.search_button = QPushButton("Search")
        self.back_button = QPushButton("Back")

        main_layout.addWidget(QLabel("Brand: "))
        main_layout.addWidget(self.nonkey_field)
        main_layout.addWidget(self.search_button)
        main_layout.addWidget(self.back_button)

        main_layout.addStretch(1)

class SearchResultWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setWindowTitle("carDB: SearchResult")
        self.setGeometry(500, 200, 800, 500)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout(central_widget)

        self.result_table = QTableWidget(self)
        self.result_table.setColumnCount(5)
        self.result_table.setHorizontalHeaderLabels(["ID", "Brand", "Model", "Year", "Color"])
        
        self.back_button = QPushButton("Back")

        main_layout.addWidget(self.result_table)
        main_layout.addWidget(self.back_button)
        main_layout.addStretch(1)




class DeleteWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        
        self.setWindowTitle("carDB")
        self.setGeometry(500, 200, 800, 500)

class ClearWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setupUI()
    
    def setupUI(self):

        self.setWindowTitle("carDB")
        self.setGeometry(500, 200, 800, 500)

class UpdateWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):

        self.setWindowTitle("carDB")
        self.setGeometry(500, 200, 800, 500)

class InsertWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setWindowTitle("carDB")
        self.setGeometry(500, 200, 800, 500)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        main_layout = QVBoxLayout(central_widget)

        self.id_field = QLineEdit()
        self.brand_field = QLineEdit()
        self.model_field = QLineEdit()
        self.year_field = QLineEdit()
        self.color_field = QLineEdit()

        self.insert_button = QPushButton("Insert")
        self.back_button = QPushButton("Back")

        field_layout = QHBoxLayout()
        field_layout.setSpacing(0)
        field_layout.setContentsMargins(0, 0, 0, 0)

        field_layout.addWidget(QLabel("ID: "))
        field_layout.addWidget(self.id_field)
        field_layout.addWidget(QLabel("BRAND: "))
        field_layout.addWidget(self.brand_field)
        field_layout.addWidget(QLabel("MODEL: "))
        field_layout.addWidget(self.model_field)
        field_layout.addWidget(QLabel("YEAR: "))
        field_layout.addWidget(self.year_field)
        field_layout.addWidget(QLabel("COLOR: "))
        field_layout.addWidget(self.color_field)

        main_layout.addLayout(field_layout)
        main_layout.addWidget(self.insert_button)
        main_layout.addWidget(self.back_button)

        field_layout.addStretch(1)
        main_layout.addStretch(1)




        
