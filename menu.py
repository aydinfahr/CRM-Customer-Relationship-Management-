from PyQt6.QtWidgets import QApplication
from mentor_menu import MentorPage

app = QApplication([])
window = MentorPage()
window.show()
app.exec()    # exec_() not found !???
