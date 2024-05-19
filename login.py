# from PyQt6.QtWidgets import *  # * gerekli mi?
from PyQt6.QtWidgets import QMainWindow
from UI_Files.login_ui import Ui_MainWindow

from menu import MenuPage


class LoginPage(QMainWindow):
     
    def __init__(self):
        super().__init__()
        self.login_window = Ui_MainWindow()
        self.login_window.setupUi(self)
        
        self.is_admin = False
        self.users = None
        self.open_menu_window = None
        

        self.login_window.pushButtonLogin.clicked.connect(self.login)
        #show password eklenebilir
        #enter tusuna basma ile ilgili ozellik eklenebilir


    def login(self):
        username = self.login_window.lineEditUsername.text()
        password = self.login_window.lineEditPassword.text()
        
        for user in self.users[1:]:
            self.is_admin = user[2] == 'admin'

            if username == user[0] and password == user[1]:            
                self.open_menu_window = MenuPage(self.is_admin)
                self.hide()  
                self.open_menu_window.show()
   
            elif not username and not password:
                self.login_window.labelErrorMessage.setText("<b>Please enter username and password</b>")
            elif not username:
                self.login_window.labelErrorMessage.setText("<b>Please enter username</b>")
            elif not password:
                self.login_window.labelErrorMessage.setText("<b>Please enter password</b>")  
            else:
                self.login_window.labelErrorMessage.setText("<b>Username or password is incorrect!</b>")
                # self.login_window.lineEditUsername.setText("")  #girisleri sifirla
                # self.login_window.lineEditPassword.setText("")




       

    
        

        
