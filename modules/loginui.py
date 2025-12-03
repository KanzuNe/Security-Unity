
import sys
from PyQt5.QtWidgets import QApplication, QMessageBox, QMainWindow, QTableWidgetItem, QComboBox
from PyQt5 import uic
from PyQt5.QtCore import Qt
import json

class Users:
     pass_list =[]
     def __init__(self,website, username, password):
          self.website = website
          self.username = username
          self.password = password

class PopUp(QMainWindow):
    def __init__(self, username, main_window, mode="add"):
        super().__init__()
        uic.loadUi(r"ui\popup.ui", self)
        self.mode= mode
        self.current_user = username
        self.mainwindow = main_window
        self.setWindowTitle(f"Add/Update")
        #events
        if mode == "add":
            self.pushButton.clicked.connect(self.add)
        else:
            self.load_user_to_fields()
            self.pushButton.clicked.connect(self.edit)

    def edit(self):
        selected_row = self.mainwindow.table.currentRow()
        if selected_row >= 0:
            user = Users.pass_list[selected_row]
            user.website = self.website.text().strip()
            user.username = self.username.text().strip()
            user.password = self.password.text().strip()
            save_pass(self.current_user)
            self.mainwindow.update_table()
            self.close()
        
    def add(self):
        website = self.website.text().strip()
        username = self.username.text().strip()
        password = self.password.text().strip()
        if website and username and password:
            Users.pass_list.append(Users(website, username, password))
            save_pass(self.current_user)
            self.mainwindow.update_table()
            self.close()
        else:
            QMessageBox.warning(self, "Warning", "Fill All Infos!")

    def load_user_to_fields(self):
        selected_row = self.mainwindow.table.currentRow()
        if selected_row >= 0:
            user = Users.pass_list[selected_row]
            self.website.setText(user.website)
            self.username.setText(user.username)
            self.password.setText(user.password)    

class MainUi(QMainWindow):
    def __init__(self, username):
        super().__init__()
        uic.loadUi(r"ui\passui.ui", self)
        self.current_user = username
        self.setWindowTitle(f"Password Manager - {username}")
        self.Welcome.setText(f"Welcome {username}!")
        self.table.setSortingEnabled(True)
        load_pass(username)
        self.update_table()
        #events
        self.SearchButton.clicked.connect(self.update_table_search)
        self.AddNew.clicked.connect(self.open_popup_add)
        self.Update.clicked.connect(self.open_popup_edit)
        self.Delete.clicked.connect(self.delete_user)
        self.GenerateRan.clicked.connect(self.generate_random)
        self.table.itemSelectionChanged.connect(self.update_pass_strength)
        #Password Strength
        self.bar.setValue(0)

    def update_table(self):
        self.table.setRowCount(len(Users.pass_list))
        for index, f in enumerate(Users.pass_list):
             self.table.setItem(index, 0, QTableWidgetItem(f.website))
             self.table.setItem(index, 1, QTableWidgetItem(f.username))
             self.table.setItem(index, 2, QTableWidgetItem(f.password))
        self.table.clearSelection()
        self.table.setCurrentItem(None)
        self.bar.setValue(0)

    def update_table_search(self):
        self.filtered_list = []
        search_text = self.search_bar.text().strip().lower()
        if not search_text:
            self.update_table()
            return
        for s in Users.pass_list:
            if search_text in s.website.lower() or search_text in s.username.lower() or search_text in s.password.lower():
                self.filtered_list.append(s)
        self.table.setRowCount(len(self.filtered_list))  
        for index, s in enumerate(self.filtered_list):
            self.table.setItem(index, 0, QTableWidgetItem(s.website))
            self.table.setItem(index, 1, QTableWidgetItem(s.username))
            self.table.setItem(index, 2, QTableWidgetItem(s.password))
        self.table.clearSelection()
        self.table.setCurrentItem(None)

    def delete_user(self):
        selected_row = self.table.currentRow()
        if selected_row >=0:
            Users.pass_list.pop(selected_row)
            save_pass(self.current_user)
            self.update_table()
        else:
            QMessageBox.warning(self, "Warning", "Please select a row to delete")   

    def generate_random(self):
        selected_row = self.table.currentRow()
        if selected_row >=0:
            User = Users.pass_list[selected_row]
            User.password = random_char()
            save_pass(self.current_user)
            self.update_table()


    def open_popup_add(self):
        self.table.clearSelection()
        self.table.setCurrentItem(None)
        self.bar.setValue(0)
        self.popup = PopUp(self.current_user, self, mode="add")
        self.popup.show()
    
    def open_popup_edit(self):
        selected_row = self.table.currentRow()
        if selected_row >=0:
            self.table.clearSelection()
            self.table.setCurrentItem(None)
            self.bar.setValue(0)
            self.popup = PopUp(self.current_user, self, mode="edit")
            self.popup.show()
        else:
            QMessageBox.warning(self, "Warning", "Please select a row to edit")

    def update_pass_strength(self):
        strength = self.checking_requirements()
        self.bar.setValue(strength)
        selected_row = self.table.currentRow()
        if selected_row >=0:
            if strength < 40:
                self.bar.setStyleSheet("QProgressBar::chunk { background-color: red; }")
                self.status.setText("Status: Bad >:(")
            elif strength < 70:
                self.bar.setStyleSheet("QProgressBar::chunk { background-color: yellow; }")
                self.status.setText("Status: Acceptable...")
            else:
                self.status.setText("Status: Good!")
                self.bar.setStyleSheet("QProgressBar::chunk { background-color: green; }")
        else:
            self.bar.setValue(0)
            self.status.setText("Status: Select a password")

    
    def checking_requirements(self):
        selected_row = self.table.currentRow()
        if selected_row >=0:
            value = 0
            User = Users.pass_list[selected_row]
            if len(User.password) >=12:
                value +=20
            has_upper = any(char.isupper() for char in User.password)
            has_lower = any(char.islower() for char in User.password)
            has_digit = any(char.isdigit() for char in User.password)
            has_special = any(not char.isalnum() for char in User.password)
            if has_upper:
                value += 20
            if has_lower:
                value += 20
            if has_digit:
                value += 20
            if has_special:
                value += 20
            return min(value, 100)
        return 0




    
        
        
class LoginUi(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(r"ui\loginui.ui", self)
        self.setWindowTitle(f"Log In")
        self.userlist = {}
        self.load_userlist()
        self.UserChoice.setCurrentText("")
        #events
        self.EnterVault.clicked.connect(self.create_new_user)
    
    def load_userlist(self):
        with open (r"data\config\username.json", "r+", encoding="utf-8") as f:
            data = json.load(f)
        self.user_list = data
        for index, key in enumerate(self.user_list):
            self.UserChoice.insertItem(index, key )
        
    def create_new_user(self):
        current_username = self.UserChoice.currentText()
        if current_username in self.user_list:
            self.validate()
        else:
            password = self.PassEnter.text()
            current_dic = {}
            current_dic = self.user_list
            current_dic[current_username] = password
            with open (r"data\config\username.json", "w", encoding="utf-8") as f:
                json.dump(current_dic, f, separators=(',', ':'))
            self.open_mainui()

    def validate(self):
        current_username = self.UserChoice.currentText()
        password = self.PassEnter.text()
        if (current_username, password) in self.user_list.items():
            self.open_mainui()
        else:
            QMessageBox.warning(self, "Warning", "Wrong Password!")                    

    def open_mainui(self):
        current_username = self.UserChoice.currentText()
        self.mainui = MainUi(current_username)
        self.mainui.show()
        self.hide()
        

#Global
def load_pass(username):
    Users.pass_list.clear()
    try:
        CSV_FILE= f"data/vaults/{username}.csv"
        with open (CSV_FILE, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    website, username_entry, password = line.split(",")
                    Users.pass_list.append(Users(website, username_entry, password))
    except FileNotFoundError:
        with open (CSV_FILE, "w", encoding="utf-8") as f:
            f.write("")

def save_pass(username):
        CSV_FILE= f"data/vaults/{username}.csv"
        with open (CSV_FILE, "w", encoding="utf-8") as f:
            for num in Users.pass_list:
                f.write(f"{num.website},{num.username},{num.password}\n")

def random_char():
    import random
    import string
    all_chars = string.ascii_letters + string.digits + "!@#$%^&*()_?><}{}"
    chars = []
    for _ in range(12):
        chars.append(random.choice(all_chars))
    return ''.join(chars)





if __name__ == "__main__":
    app = QApplication(sys.argv)
    loginui = LoginUi()
    loginui.show()
    sys.exit(app.exec_())

