
from PyQt6.QtWidgets import QMainWindow,QLineEdit
from UI_Files.login_ui import Ui_MainWindow
from menu import MenuPage
import main


class LoginPage(QMainWindow):  
    def __init__(self):
        super().__init__()
        self.login_window = Ui_MainWindow()
        self.login_window.setupUi(self)
        self.is_admin = False
        self.users = None
        
        self.login_window.pushButtonLogin.clicked.connect(self.login)
        self.login_window.checkBox.clicked.connect(self.show_password)
        #enter tusuna basma ile ilgili ozellik eklenebilir

    def show_password(self):
        if self.login_window.checkBox.isChecked():
            self.login_window.lineEditPassword.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.login_window.lineEditPassword.setEchoMode(QLineEdit.EchoMode.Password)

    def login(self):
        username = self.login_window.lineEditUsername.text().strip()
        password = self.login_window.lineEditPassword.text().strip()

        self.login_window.labelErrorMessage.clear()

        if not username and not password:
            self.login_window.labelErrorMessage.setText("<b>Please enter username and password</b>")
            return
        elif not username:
            self.login_window.labelErrorMessage.setText("<b>Please enter username</b>")
            return
        elif not password:
            self.login_window.labelErrorMessage.setText("<b>Please enter password</b>")
            return

        for user in self.users[1:]:
            if username == user[0] and password == user[1]:
                self.is_admin = user[2] == 'admin'
                self.open_menu_window = MenuPage(self.is_admin)
                self.hide()
                self.open_menu_window.show()
                return

        self.login_window.labelErrorMessage.setText("<b>Username or password is incorrect!</b>")
        self.login_window.lineEditUsername.clear()
        self.login_window.lineEditPassword.clear()

                




       

    
        

        
