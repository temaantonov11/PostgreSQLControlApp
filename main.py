from databaseAPI import *
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from coreGUI import interface






def main():
    app = QApplication(sys.argv)
    window = interface.StartWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

