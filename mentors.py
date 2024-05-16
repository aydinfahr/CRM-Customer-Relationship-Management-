from PyQt6.QtWidgets import *
from PyQt6.QtWidgets import QMainWindow
from UI_Files.mentors_ui import Ui_MainWindow

class MentorPage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.mentor_window = Ui_MainWindow()
        self.mentor_window.setupUi(self)