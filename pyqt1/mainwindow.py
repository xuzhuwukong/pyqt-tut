
from PyQt5.QtWidgets import QApplication, QMainWindow
from pyqt1.untitled import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)