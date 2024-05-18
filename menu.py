from PyQt6.QtWidgets import QMainWindow #,QApplication yada *
from UI_Files.menu_ui import Ui_MainWindow



class MenuPage(QMainWindow):
    def __init__(self, is_admin):
        super().__init__()  ##is_admin parametresi ekleyince hata veriyor
        self.is_admin = is_admin
        self.menu_window = Ui_MainWindow()
        self.menu_window.setupUi(self)
        
        
        ## gecici!
        if not self.is_admin:
            self.menu_window.pushButtonAdminMenu.close()

        self.open_applications_window = None
        self.open_interviews_window = None
        self.open_mentors_window = None
        self.open_management_window = None

        self.menu_window.pushButtonApplications.clicked.connect(self.go_applications_page)
        self.menu_window.pushButtonInterviews.clicked.connect(self.go_interviews_page)
        self.menu_window.pushButtonMentorMeetings.clicked.connect(self.go_mentors_page)
        self.menu_window.pushButtonAdminMenu.clicked.connect(self.go_managament_page)
        self.menu_window.pushButtonExit.clicked.connect(self.app_exit)


    def go_applications_page(self):
        from applications import ApplicationsPage
        self.open_applications_window = ApplicationsPage()
        self.hide()
        self.open_applications_window.show()

    def go_interviews_page(self):
        from interviews import InterviewsPage
        self.open_interviews_window = InterviewsPage()
        self.hide()
        self.open_interviews_window.show()

    def go_mentors_page(self):
        from mentors import MentorsPage
        self.open_mentors_window = MentorsPage()
        self.hide()
        self.open_mentors_window.show()
    
    def go_managament_page(self):
        from management import ManagementPage
        self.open_management_window = ManagementPage()
        self.hide()
        self.open_management_window.show()


    def app_exit(self):
        self.close()


    
