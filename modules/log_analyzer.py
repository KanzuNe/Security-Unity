import re
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QFileDialog
from PyQt5 import uic

class Error:
    def __init__(self, timestamp, level, message):
        self.timestamp = timestamp
        self.level = level
        self.message = message
    def __str__(self):
        return(f"[{self.level}] {self.timestamp} {self.message}")
    error_list =[]



patterns = [
    r"\[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\] \[(INFO|ERROR|WARNING|DEBUG|CRITICAL)\][ -]*(.+)",  # [timestamp] [level] - message
    r"\((\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\) \((INFO|ERROR|WARNING|DEBUG|CRITICAL)\)[ -]*(.+)",  # (timestamp) (level) - message
    r"\[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\] \((INFO|ERROR|WARNING|DEBUG|CRITICAL)\)[ -]*(.+)",  # [timestamp] (level) - message
    r"\((\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\) \[(INFO|ERROR|WARNING|DEBUG|CRITICAL)\][ -]*(.+)",  # (timestamp) [level] - message
    r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (INFO|ERROR|WARNING|DEBUG|CRITICAL)[ -]*(.+)",  # timestamp level - message (no brackets)
    r"\[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\] \[(INFO|ERROR|WARNING|DEBUG|CRITICAL)\]:[ ]*(.+)",  # [timestamp] [level]: message (with colon)
    r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) - (INFO|ERROR|WARNING|DEBUG|CRITICAL) - (.+)",  # timestamp - level - message (dash separators)
    r"\[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\] \((INFO|ERROR|WARNING|DEBUG|CRITICAL)\) (.+)",  # [timestamp] (level) message (no separator)
    r"\((\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\) \[(INFO|ERROR|WARNING|DEBUG|CRITICAL)\] (.+)",  # (timestamp) [level] message (no separator)
    
]




class MyWindow(QMainWindow):
    info_counter = 0
    error_counter = 0
    warning_counter = 0
    debug_counter = 0
    critical_counter = 0
    def __init__(self):
        super().__init__()
        # Load the UI file
        uic.loadUi(r"ui\log_analyzer.ui", self)
        self.error_list = Error.error_list
        
        #Connect Button
        self.search_button.clicked.connect(self.update_table_search)
        self.choose_file.clicked.connect(self.inputButton)
    def inputButton(self):
        Error.error_list.clear()
        self.info_counter = 0
        self.error_counter = 0
        self.warning_counter = 0
        self.debug_counter = 0
        self.critical_counter = 0

        filename, _ = QFileDialog.getOpenFileName(parent=self, caption='Open Log File', directory ='.', filter='Log Files (*.log);;Text Files (*.txt)')
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                for pattern in patterns:
                    match= re.search(pattern, line)
                    if match:
                        timestamp = match.group(1)
                        level = match.group(2)
                        message = match.group(3)
                        Error.error_list.append(Error(timestamp, level, message))
                        if level.lower() == "info":
                                self.info_counter += 1
                        elif level.lower() == "error":
                                self.error_counter += 1
                        elif level.lower() == "warning":
                                self.warning_counter += 1
                        elif level.lower() == "debug":
                                self.debug_counter += 1
                        elif level.lower() == "critical":
                                self.critical_counter += 1
            self.update_table()
            self.update_counter()
    
    def update_counter(self):
        level = [("INFO", self.info_counter),("ERROR", self.error_counter),("WARNING", self.warning_counter),("DEBUG", self.debug_counter),("CRITICAL", self.critical_counter)]
        self.counter.setRowCount(5)
        for index, (level, count) in enumerate(level):
            self.counter.setItem(index, 0, QTableWidgetItem(level))
            self.counter.setItem(index, 1, QTableWidgetItem(str(count)))
          
    
    def update_table(self):
        self.log_table.setRowCount(len(self.error_list))
        for index, error in enumerate(self.error_list):
            self.log_table.setItem(index, 0, QTableWidgetItem(error.timestamp))
            self.log_table.setItem(index, 1, QTableWidgetItem(error.level))
            self.log_table.setItem(index, 2, QTableWidgetItem(error.message))
        self.log_table.sortItems(0, order=QtAscendingOrder)
        self.log_table.sortItems(1, order=QtAscendingOrder)
        self.log_table.sortItems(2, order=QtAscendingOrder)

    def update_table_search(self):
        self.filtered_list = []
        search_text = self.search_bar.toPlainText().strip().lower()
        if not search_text:
            self.show_all()
            return

        for error in self.error_list:
            if search_text in error.timestamp.lower() or search_text in error.level.lower() or search_text in error.message.lower():
                self.filtered_list.append(error)
        self.log_table.setRowCount(len(self.filtered_list))  
        for index, error in enumerate(self.filtered_list):
            self.log_table.setItem(index, 0, QTableWidgetItem(error.timestamp))
            self.log_table.setItem(index, 1, QTableWidgetItem(error.level))
            self.log_table.setItem(index, 2, QTableWidgetItem(error.message))

    def show_all(self):
        self.update_table()
        self.search_bar.clear()
        self.statusbar.showMessage(f"Reset Filter!")

    



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
    
    