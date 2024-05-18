from PyQt6.QtWidgets import QMainWindow
from UI_Files.management_ui import Ui_MainWindow


class ManagementPage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.management_window = Ui_MainWindow()
        self.management_window.setupUi(self)

        self.open_menu_window = None
    
        self.management_window.pushButtonExit.clicked.connect(self.app_exit)
        self.management_window.pushButtonBackMainPage.clicked.connect(self.back_menu)

    def back_menu(self):
        from menu import MenuPage
        self.open_menu_window = MenuPage(True) ##gecici true
        self.hide()  
        self.open_menu_window.show()

    def app_exit(self):
        self.close()
    