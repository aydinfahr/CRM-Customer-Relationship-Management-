
from PyQt6.QtWidgets import QMainWindow
from UI_Files.mentors_ui import Ui_MainWindow
import main

class MentorsPage(QMainWindow):
    def __init__(self, is_admin):
        super().__init__()
        self.mentor_window = Ui_MainWindow()
        self.mentor_window.setupUi(self)
        

        self.is_admin = is_admin


        self.mentor_window.tableWidget.setColumnWidth(1, 120)
        self.mentor_window.tableWidget.setColumnWidth(2, 120)
        self.mentor_window.tableWidget.setColumnWidth(3, 90)
        self.mentor_window.tableWidget.setColumnWidth(4, 380)
        self.mentor_window.tableWidget.setColumnWidth(5, 400)
        


        self.open_menu_window = None

        self.mentor_window.pushButtonExit.clicked.connect(self.app_exit)
        self.mentor_window.pushButtonBackMainPage.clicked.connect(self.back_menu)
        self.mentor_window.pushButtonAllMeetings.clicked.connect(self.load_all_meetings)


        

    def load_all_meetings(self):
        self.meetings = main.connect_spreadsheet("Mentor")
        main.load_table(self.mentor_window,self.meetings)       
        

    def back_menu(self):
        from menu import MenuPage
        
        self.open_menu_window = MenuPage(self.is_admin)  
        self.hide()
        self.open_menu_window.show()

    def app_exit(self):
        self.close()
    