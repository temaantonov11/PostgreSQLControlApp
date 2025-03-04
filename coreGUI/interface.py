import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel,
                             QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QPushButton,
                             QCheckBox, QRadioButton, QButtonGroup, QLineEdit)
from PyQt5.QtCore import Qt

class StartWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("carDB")
        self.setGeometry(100, 100, 400, 300)