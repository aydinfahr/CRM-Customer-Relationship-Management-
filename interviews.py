
from PyQt6.QtWidgets import QMainWindow
from UI_Files.interviews_ui import Ui_MainWindow


class InterviewsPage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.interviews_page = Ui_MainWindow()
        self.interviews_page.setupUi(self)
