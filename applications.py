# from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow
from UI_Files.applications_ui import Ui_MainWindow


class ApplicationsPage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.applications_window = Ui_MainWindow()
        self.applications_window.setupUi(self)

    
