from PyQt6.QtWidgets import *
from PyQt6.QtWidgets import QMainWindow
from UI_Files.login_ui import Ui_MainWindow

class LoginPage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.login_window = Ui_MainWindow()
        self.login_window.setupUi(self)