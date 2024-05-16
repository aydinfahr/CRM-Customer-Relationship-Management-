from PyQt6.QtWidgets import QApplication
from login import LoginPage

app = QApplication([])
login_window = LoginPage()
login_window.show()
app.exec()