from PyQt6.QtWidgets import QMainWindow
from UI_Files.management_ui import Ui_MainWindow


class ManagementPage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.management_window = Ui_MainWindow()
        self.management_window.setupUi(self)