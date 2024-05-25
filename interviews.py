
from PyQt6.QtWidgets import QMainWindow
from UI_Files.interviews_ui import Ui_MainWindow
import main
from menu import MenuPage


class InterviewsPage(QMainWindow):
    def __init__(self,is_admin):
        super().__init__()
        self.interviews_window = Ui_MainWindow()
        self.interviews_window.setupUi(self)
        self.is_admin = is_admin
        self.interviews_file = None

        main.set_column_width(self.interviews_window, {0:200, 1:200, 2:200})

        self.interviews_window.pushButtonSearch.clicked.connect(self.search)
        self.interviews_window.pushButtonReceivedAssignment.clicked.connect(self.get_who_received_assignment)
        self.interviews_window.pushButtonSubmittedAssignment.clicked.connect(self.get_who_submitted_assignment)
        self.interviews_window.pushButtonBackMainPage.clicked.connect(self.back_menu)
        self.interviews_window.pushButtonExit.clicked.connect(self.app_exit)


    def load_data(self):
        if self.interviews_file == None:
            self.interviews_file = main.connect_spreadsheet("Mulakatlar")

    def search(self):
        self.load_data()
        input_text = self.interviews_window.lineEditSearch.text().lower()
        if input_text == '':
            self.interviews_window.lineEditSearch.setPlaceholderText("Enter the text to search!")
            return     
        search_result = []
        for row in self.interviews_file[1:]:       
            applicant = row[0].lower().split()
            if any(part.startswith(input_text) for part in applicant):
                search_result.append(row)

        self.interviews_window.tableWidget.clearContents()
        main.print_table(self.interviews_window, search_result)

    def get_who_received_assignment(self):
        self.load_data()
        file_received = []
        for row in self.interviews_file[1:]:
            if  row[1]:
                file_received.append(row)
        main.print_table(self.interviews_window, file_received)

    def get_who_submitted_assignment(self):
        self.load_data()
        file_submitted = []
        for row in self.interviews_file[1:]:
            if  row[2]:
                file_submitted.append(row)
        main.print_table(self.interviews_window, file_submitted)


    def back_menu(self):
        self.open_menu_window = MenuPage(self.is_admin)  
        self.hide()
        self.open_menu_window.show()

    def app_exit(self):
        self.close()
    
