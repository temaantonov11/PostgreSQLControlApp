import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel,
                             QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QPushButton,
                             QCheckBox, QRadioButton, QButtonGroup, QLineEdit)
from PyQt5.QtCore import Qt

class StartWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        
        self.setWindowTitle("carDB")
        self.setGeometry(500, 200, 800, 500)
        
        central_widget = QWidget()
        
        self.setCentralWidget(central_widget)
        central_widget.setFixedSize(200, 200)
        

        container_widget = QWidget()
        container_widget.setFixedSize(200, 120)
        role_widget = QWidget()
        role_widget.setFixedSize(200, 120)
        init_widget = QWidget()
        init_widget.setFixedSize(200, 100)
        
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

        self.username_field = QLineEdit(self)
        self.password_field = QLineEdit(self)

        self.admin_option = QRadioButton("Admin")
        self.guest_option = QRadioButton("Guest")

        self.login_option = QRadioButton("log in")
        self.registry_option = QRadioButton("sign up")

        self.role_group = QButtonGroup()
        self.role_group.addButton(self.admin_option, 1)
        self.role_group.addButton(self.guest_option, 2)

        self.init_group = QButtonGroup()
        self.init_group.addButton(self.login_option, 1)
        self.init_group.addButton(self.registry_option, 2)

        role_layout = QHBoxLayout()
        role_layout.setSpacing(0)
        role_layout.setContentsMargins(0, 0, 0, 0)

        auth_layout = QVBoxLayout()
        auth_layout.setSpacing(0)
        auth_layout.setContentsMargins(0, 0, 0, 0)

        init_layout = QHBoxLayout()
        init_layout.setSpacing(0)
        init_layout.setContentsMargins(0, 0, 0, 0)

        auth_layout.addWidget(QLabel('Username: '))
        auth_layout.addWidget(self.username_field)
        auth_layout.addWidget(QLabel('Password: '))
        auth_layout.addWidget(self.password_field)

        role_layout.addWidget(self.admin_option)
        role_layout.addWidget(self.guest_option)        
        
        init_layout.addWidget(self.login_option)
        init_layout.addWidget(self.registry_option)

        container_widget.setLayout(auth_layout)
        role_widget.setLayout(role_layout)
        init_widget.setLayout(init_layout)
        
        main_layout = QVBoxLayout()
        main_layout.setSpacing(0)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.addWidget(container_widget, alignment=Qt.AlignCenter)
        main_layout.addWidget(role_widget, alignment=Qt.AlignCenter)
        main_layout.addWidget(init_widget, alignment=Qt.AlignCenter)
        central_widget.setLayout(main_layout)
        
        


        
