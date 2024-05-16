# from PyQt6.QtWidgets import *  # * gerekli mi?
from PyQt6.QtWidgets import QMainWindow
from UI_Files.login_ui import Ui_MainWindow
from menu import MenuPage

class LoginPage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.login_window = Ui_MainWindow()
        self.login_window.setupUi(self)

        self.open_menu_window = MenuPage()

        self.login_window.pushButtonLogin.clicked.connect(self.login)

    def login(self):
        username = self.login_window.lineEditUsername.text()
        password = self.login_window.lineEditPassword.text()

        if username == "a" and password == "1":
            self.hide()  
            self.open_menu_window.show()
        else:
            self.login_window.labelErrorMessage.setText("<b>Your email or password is incorrect.</b>")


       

    
        

        
