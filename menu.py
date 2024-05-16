from PyQt6.QtWidgets import QMainWindow #,QApplication
from UI_Files.menu_ui import Ui_MainWindow

class MenuPage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.menu_window = Ui_MainWindow()
        self.menu_window.setupUi(self)
