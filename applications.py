# from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow
from UI_Files.applications_ui import Ui_MainWindow


class ApplicationsPage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.applications_window = Ui_MainWindow()
        self.applications_window.setupUi(self)


        self.applications_window.pushButtonBackMainPage.clicked.connect(self.back_menu)
        self.applications_window.pushButtonExit.clicked.connect(self.app_exit)

    def back_menu(self):
        from menu import MenuPage
        
        self.open_menu_window = MenuPage(True)  ## True gecici!
        self.hide()
        self.open_menu_window.show()



    def app_exit(self):
        self.close()
    

    
