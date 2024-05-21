from PyQt6.QtWidgets import QMainWindow
from UI_Files.mentors_ui import Ui_MainWindow
import main

class MentorsPage(QMainWindow):
    def __init__(self, is_admin):
        super().__init__()
        self.mentor_window = Ui_MainWindow()
        self.mentor_window.setupUi(self)
        self.is_admin = is_admin
        self.meetings = None

        self.mentor_window.tableWidget.setColumnWidth(1, 120)
        self.mentor_window.tableWidget.setColumnWidth(2, 120)
        self.mentor_window.tableWidget.setColumnWidth(3, 90)
        self.mentor_window.tableWidget.setColumnWidth(4, 380)
        self.mentor_window.tableWidget.setColumnWidth(5, 400)
        self.mentor_window.tableWidget.setColumnWidth(6, 80)
        self.mentor_window.tableWidget.setColumnWidth(7, 1000)  

        self.mentor_window.pushButtonAllMeetings.clicked.connect(self.print_all_meetings)
        self.mentor_window.pushButtonSearch.clicked.connect(self.search)
        self.mentor_window.lineEditSearch.returnPressed.connect(self.search)
        self.mentor_window.comboBox.currentIndexChanged.connect(self.filter_table)
        self.mentor_window.pushButtonBackMainPage.clicked.connect(self.back_menu)
        self.mentor_window.pushButtonExit.clicked.connect(self.app_exit)
  

    def load_file(self):
        self.meetings = main.connect_spreadsheet("Mentor")
                

    def print_all_meetings(self):
        if self.meetings == None:     
            self.load_file()
        main.print_table(self.mentor_window, self.meetings)  

    def search(self):
        input_text = self.mentor_window.lineEditSearch.text().lower()
        if input_text == '':
            self.mentor_window.lineEditSearch.setPlaceholderText("Enter the text to search!")
            return
        if self.meetings == None:     
            self.load_file()

        search_result = [[]]
        for row in self.meetings[1:]:       
            applicant = row[1].lower().split()
            mentor = row[2].lower().split()
            mixed_names = applicant + mentor

            if any(part.startswith(input_text) for part in mixed_names):
                search_result.append(row)

        self.mentor_window.tableWidget.clearContents()
        main.print_table(self.mentor_window, search_result)

    def filter_table(self):
        if self.meetings == None:
             self.load_file()
        selected_item = self.mentor_window.comboBox.currentText()
        filtered_table = [[]]
        for row in self.meetings[1:]:
            if selected_item.lower().strip() == row[4].lower().strip():
                filtered_table.append(row)
        main.print_table(self.mentor_window, filtered_table)


    def back_menu(self):
        from menu import MenuPage
        
        self.open_menu_window = MenuPage(self.is_admin)  
        self.hide()
        self.open_menu_window.show()

    def app_exit(self):
        self.close()
    