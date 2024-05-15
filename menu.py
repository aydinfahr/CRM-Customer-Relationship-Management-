from PyQt6.QtWidgets import QApplication
from mentors import MentorPage

app = QApplication([])
window = MentorPage()
window.show()
app.exec()    # exec_() not found !???
