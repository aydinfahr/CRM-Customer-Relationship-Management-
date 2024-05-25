
from PyQt6.QtWidgets import QApplication, QTableWidgetItem
import gspread


def connect_spreadsheet(file):
    service_acc = gspread.service_account(filename="key.json")
    spreadsheet = service_acc.open(file)
    worksheet = spreadsheet.get_worksheet(0)  
    items = worksheet.get_all_values()
    return items

def set_column_width(window, dict_columnwidth):
    for i, width in dict_columnwidth.items():
        window.tableWidget.setColumnWidth(i, width)

def print_table(window, file):
    table_widget = window.tableWidget
    table_widget.clearContents()
    table_widget.setRowCount(len(file))
    
    row_index = 0
    for row in file:
        column_index = 0
        for column in row:
            item = QTableWidgetItem(str(column))
            table_widget.setItem(row_index, column_index, item)
            column_index += 1
        row_index += 1
                
                 
def main():
    from login import LoginPage
    app = QApplication([])
    login_window = LoginPage()
    login_window.show()
    login_window.users = connect_spreadsheet("Kullanicilar")  
    app.exec()
    
if __name__ == "__main__":
    main()
