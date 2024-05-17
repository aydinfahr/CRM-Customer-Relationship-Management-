from PyQt6.QtWidgets import QMainWindow #,QApplication yada *
from UI_Files.menu_ui import Ui_MainWindow

from applications import ApplicationsPage
from interviews import InterviewsPage
from mentors import MentorsPage
#from management import ManagementPage



class MenuPage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.menu_window = Ui_MainWindow()
        self.menu_window.setupUi(self)

        self.open_applications_window = ApplicationsPage()
        self.open_interviews_window = InterviewsPage()
        self.open_mentors_window = MentorsPage()
        #self.open_management_window = ManagementPage()


        self.menu_window.pushButtonInterviews.clicked.connect(self.go_interviews_page)
        self.menu_window.pushButtonApplications.clicked.connect(self.go_applications_page)
        self.menu_window.pushButtonMentorMeetings.clicked.connect(self.go_mentors_page)
        #self.menu_window.pushButtonAdminMenu.clicked.connect(self.go_management_page)

    def go_applications_page(self):
        self.hide()
        self.open_applications_window.show()

    def go_interviews_page(self):
        self.hide()
        self.open_interviews_window.show()

    def go_mentors_page(self):
        self.hide()
        self.open_mentors_window.show()
    
    #def go_managament_page(self): ...
    
