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

        container_widget = QWidget()
        container_widget.setFixedSize(200, 120)
        
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

         
        
        auth_layout = QVBoxLayout()
        auth_layout.setSpacing(0)
        auth_layout.setContentsMargins(0, 0, 0, 0) 

        auth_layout.addWidget(QLabel('Username: '))
        auth_layout.addWidget(self.username_field)
        auth_layout.addWidget(QLabel('Password: '))
        auth_layout.addWidget(self.password_field)
        
        container_widget.setLayout(auth_layout)

        main_layout = QVBoxLayout()
        main_layout.addWidget(container_widget, alignment=Qt.AlignCenter)
        central_widget.setLayout(main_layout)
        


        
