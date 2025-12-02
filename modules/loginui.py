
import sys
from PyQt5.QtWidgets import QApplication, QMessageBox, QMainWindow, QTableWidgetItem, QComboBox
from PyQt5 import uic
from PyQt5.QtCore import Qt
import json

class MainUi(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(r"ui\passui.ui", self)



class LoginUi(QMainWindow):
    def __init__(self):
        super().__init__()
        # Load the UI file
        uic.loadUi(r"ui\loginui.ui", self)
        self.userlist = {}
        self.load_userlist()
        self.UserChoice.setCurrentText("")
        
        self.EnterVault.clicked.connect(self.create_new_user)
        self.EnterVault.clicked.connect(self.validate)
    
    def load_userlist(self):
        with open (r"data\config\username.json", "r+", encoding="utf-8") as f:
            data = json.load(f)
        self.user_list = data
        for index, key in enumerate(self.user_list):
            self.UserChoice.insertItem(index, key )

        
    def create_new_user(self):
        current_username = self.UserChoice.currentText()
        if current_username in self.user_list:
            pass
        else:
            password = self.PassEnter.text()
            current_dic = {}
            current_dic = self.user_list
            current_dic[current_username] = password
            with open (r"data\config\username.json", "w", encoding="utf-8") as f:
                json.dump(current_dic, f, separators=(',', ':'))

    def validate(self):
        current_username = self.UserChoice.currentText()
        password = self.PassEnter.text()
        if (current_username, password) in self.user_list.items():
                self.mainui = MainUi()
                self.mainui.show()
                self.hide()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    loginui = LoginUi()
    loginui.show()
    sys.exit(app.exec_())

