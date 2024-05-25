from PyQt6.QtWidgets import QMainWindow
from UI_Files.mentors_ui import Ui_MainWindow
from menu import MenuPage
import main


class MentorsPage(QMainWindow):
    def __init__(self, is_admin):
        super().__init__()
        self.mentor_window = Ui_MainWindow()
        self.mentor_window.setupUi(self)
        self.is_admin = is_admin
        self.meetings = None

        self.dict_columnwidth = {0:100, 1:120, 2:120, 3:90, 4:380, 5:400, 6:80, 7:1000}
        self.mentor_window.tableWidget.setColumnCount(10)
        main.set_column_width(self.mentor_window, self.dict_columnwidth)

        self.mentor_window.pushButtonAllMeetings.clicked.connect(self.get_all_meetings)
        self.mentor_window.pushButtonSearch.clicked.connect(self.search)
        self.mentor_window.lineEditSearch.returnPressed.connect(self.search)
        self.mentor_window.comboBox.currentIndexChanged.connect(self.filter_table)
        self.mentor_window.pushButtonBackMainPage.clicked.connect(self.back_menu)
        self.mentor_window.pushButtonExit.clicked.connect(self.app_exit)
  

    def load_file(self):
        if self.meetings is None:
            self.meetings = main.connect_spreadsheet("Mentor")
                
    def get_all_meetings(self):
        self.load_file()

        main.print_table(self.mentor_window, self.meetings[1:])  

    def search(self):
        self.load_file()
        input_text = self.mentor_window.lineEditSearch.text().lower()
        if input_text == '':
            self.mentor_window.lineEditSearch.setPlaceholderText("Enter the text to search!")
            return     
        search_result = []
        for row in self.meetings[1:]:       
            applicant = row[1].lower().split()
            mentor = row[2].lower().split()
            mixed_names = applicant + mentor

            if any(part.startswith(input_text) for part in mixed_names):
                search_result.append(row)

        self.mentor_window.tableWidget.clearContents()
        main.print_table(self.mentor_window, search_result)

    def filter_table(self):
        self.load_file()
        selected_item = self.mentor_window.comboBox.currentText()
        filtered_table = []
        for row in self.meetings[1:]:
            if selected_item.lower().strip() == row[4].lower().strip():
                filtered_table.append(row)
        main.print_table(self.mentor_window, filtered_table)


    def back_menu(self):
        self.open_menu_window = MenuPage(self.is_admin)  
        self.hide()
        self.open_menu_window.show()

    def app_exit(self):
        self.close()
    