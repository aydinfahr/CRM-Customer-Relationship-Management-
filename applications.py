from PyQt6.QtWidgets import QMainWindow
from UI_Files.applications_ui import Ui_MainWindow
from menu import MenuPage
import main


class ApplicationsPage(QMainWindow):
    def __init__(self,is_admin):
        super().__init__()
        self.applications_window = Ui_MainWindow()
        self.applications_window.setupUi(self)
        self.is_admin = is_admin
        self.applications_file = None
        self.VIT1_file = None
        self.VIT2_file = None

        self.dict_columnwidth = {0:150, 1:150, 2:180, 3:100, 4:80, 5:120, 6:400, 7:350, 8:150, 9:150, 10:150
                                 , 11:150, 12:350, 13:350, 14:150, 15:150, 16:150, 17:400, 18:1000, 19:1000}
        self.applications_window.tableWidget.setColumnCount(30)
        main.set_column_width(self.applications_window, self.dict_columnwidth)

        self.applications_window.pushButtonSearch.clicked.connect(self.search)
        self.applications_window.pushButtonAllApplications.clicked.connect(self.get_all_applications)
        self.applications_window.pushButtonFilterApplications.clicked.connect(self.get_filtered_applications)
        self.applications_window.pushButtonDuplicateRegistrations.clicked.connect(self.get_duplicate_registrations)
        self.applications_window.pushButtonPreviousVITControl.clicked.connect(self.check_previous_VIT)
        self.applications_window.pushButtonDifferentRegistrations.clicked.connect(self.get_different_registrations)
        self.applications_window.pushButtonScheduled.clicked.connect(self.get_mentor_meeting_scheduled)
        self.applications_window.pushButtonUnscheduled.clicked.connect(self.get_mentor_meeting_unscheduled)

        self.applications_window.pushButtonBackMainPage.clicked.connect(self.back_menu)
        self.applications_window.pushButtonExit.clicked.connect(self.app_exit)


    def load_data(self):
        if not self.applications_file:
            self.applications_file = main.connect_spreadsheet("Basvurular")
        if not self.VIT1_file: 
            self.VIT1_file = main.connect_spreadsheet("VIT1")
        if not self.VIT2_file: 
            self.VIT2_file = main.connect_spreadsheet("VIT2")

    def search(self):
        self.load_data()
        input_text = self.applications_window.lineEditSearch.text().lower()
        if input_text == '':
            self.applications_window.lineEditSearch.setPlaceholderText("Enter the text to search!")
            return     
        search_result = [self.applications_file[0]]
        for row in self.applications_file[1:]:       
            applicant = row[1].lower().split()
            if any(part.startswith(input_text) for part in applicant):
                search_result.append(row)

        self.applications_window.tableWidget.clearContents()
        main.print_table(self.applications_window, search_result)

    def get_all_applications(self):
        self.load_data()
        main.print_table(self.applications_window, self.applications_file)

    def filter_files(self, object_file, duplicate=False):
        filtered_applications = [object_file[0]]
        duplicate_registrations = [object_file[0]]
        for row in object_file[1:]:
            if row in filtered_applications:
                duplicate_registrations.append(row)
            else:
                filtered_applications.append(row)

        if duplicate:
            return duplicate_registrations
        else:
            return filtered_applications    
        
    def get_filtered_applications(self):
        self.load_data()
        adjusted_file = self.filter_files(self.applications_file, duplicate=False)
        main.print_table(self.applications_window, adjusted_file)

    def get_duplicate_registrations(self):
        self.load_data()
        adjusted_file = self.filter_files(self.applications_file, duplicate=True)
        main.print_table(self.applications_window, adjusted_file)

    def check_previous_VIT(self):
        self.load_data()
        filtered_apps_file = self.filter_files(self.applications_file, duplicate=False)
        filtered_VIT1_file = self.filter_files(self.VIT1_file, duplicate=False)
        filtered_VIT2_file = self.filter_files(self.VIT2_file, duplicate=False)

        common_inVITs = []
        for i in filtered_apps_file:
            for j in filtered_VIT1_file:
                if i[2] == j[2]:
                    common_inVITs.extend([i, j])
        for i in filtered_apps_file:
            for j in filtered_VIT2_file:
                if i[2] == j[2]:
                    common_inVITs.extend([i, j])            
        for i in filtered_VIT2_file:
            for j in filtered_VIT1_file:
                if i[2] == j[2]:
                    common_inVITs.extend([i, j])
        adjusted_file = self.filter_files(common_inVITs, duplicate=True)
        main.print_table(self.applications_window, adjusted_file)

    def get_different_registrations(self):      
        self.load_data()
        filtered_apps_file = self.filter_files(self.applications_file, duplicate=False)
        filtered_VIT1_file = self.filter_files(self.VIT1_file, duplicate=False)
        filtered_VIT2_file = self.filter_files(self.VIT2_file, duplicate=False)

        for i in filtered_apps_file[1:]:
            for j in filtered_VIT1_file[1:]:
                if i[2] == j[2] :
                    try:
                        filtered_apps_file.remove(i)
                    except ValueError:
                        pass
        for i in filtered_apps_file[1:]:
            for j in filtered_VIT2_file[1:]:
                if i[2] == j[2]:
                    try:
                        filtered_apps_file.remove(i)
                    except ValueError:
                        pass
        main.print_table(self.applications_window, filtered_apps_file)

    def filter_mentor_meetings(self, scheduled):
        self.load_data()
        scheduled_list = []
        scheduled_list.append(self.applications_file[0])
        unscheduled_list = []
        unscheduled_list.append(self.applications_file[0])
        for row in self.applications_file[1:]:
            if row[20].lower().strip() == "ok":
                scheduled_list.append(row)
            else:
                unscheduled_list.append(row)
        if scheduled:
            return scheduled_list
        else:
            return unscheduled_list

    def get_mentor_meeting_scheduled(self):
        scheduled_meetings_file = self.filter_mentor_meetings(scheduled=True)
        main.print_table(self.applications_window, scheduled_meetings_file)

    def get_mentor_meeting_unscheduled(self):
        unscheduled_meetings_file = self.filter_mentor_meetings(scheduled=False)
        main.print_table(self.applications_window, unscheduled_meetings_file)

        
    def back_menu(self):
        self.open_menu_window = MenuPage(self.is_admin)  
        self.hide()
        self.open_menu_window.show()

    def app_exit(self):
        self.close()
    

    
