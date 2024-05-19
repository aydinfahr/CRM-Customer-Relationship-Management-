from PyQt6.QtWidgets import QApplication

import gspread




def connection_hub(file):
    service_acc = gspread.service_account(filename="key.json")
    spreadsheet = service_acc.open(file)
    worksheet = spreadsheet.get_worksheet(0)  
    items = worksheet.get_all_values()
    return items




if __name__ == '__main__':
    from login import LoginPage
    app = QApplication([])
    login_window = LoginPage()
    login_window.show()
    app.exec()

