
import sys
from PyQt6.uic import loadUi
from PyQt6.QtWidgets import QApplication, QDialog, QLabel, QLineEdit, QWidget
from PyQt6.QtGui import QIcon, QPixmap, QFont, QFontDatabase
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6 import QtWidgets
import mysql.connector as dbcn
from hash_engine import hash

activedb = dbcn.connect(host = "localhost", user = "root", password= "destiny012", database = "Vault8")
cur = activedb.cursor()


# JUST GETTING THIS PART RUNNING BROKE MY ASS
class LoginScreen(QDialog):
    def __init__(self):
        super(LoginScreen, self).__init__()
        label = QLabel(self)
        pixmap = QPixmap("Resources/vault8_login_wrapper_v0.1.png")
        label.setPixmap(pixmap)
        loadUi("vault8_login.ui", self)

        self.loginbutton.clicked.connect(self.loginfunction)
        self.signupbutton.clicked.connect(self.gotocreate)

    def loginfunction(self):
        user = self.usrnmfield.text()
        password = self.pwdfield.text()

        if len(user) == 0 or len(password) == 0:
            self.alertbox.setText("Please Input all Fields!")
        else:
            hashed_pwd = hash.hash(password)
            cur.execute(f"SELECT password FROM login_info WHERE username ={user}")
            result_pass = cur.fetchone()[0]
            if result_pass == password:
                print("Successfully logged in.")
                self.error.setText("")
            else:
                self.error.setText("Invalid username or password")


            # INSERT DATABASE LOGIC

    def gotocreate(self):
        signup = SignUpScreen()
        widget.addWidget(signup)
        widget.setCurrentIndex(widget.currentIndex() + 1)

class SignUpScreen(QDialog):
    def __init__(self):
        super(SignUpScreen, self).__init__()
        label = QLabel(self)
        pixmap = QPixmap("Resources/vault8_login_wrapper_v0.1.png")
        label.setPixmap(pixmap)
        loadUi("vault8_signup.ui",self)

        self.signupbutton.clicked.connect(self.SignUpFunction)
        self.returnbtn.clicked.connect(self.gotologin)

    def gotologin(self):
        login = LoginScreen()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex() - 1)


    def SignUpFunction(self):
        user = self.usrnmfield.text()
        email = self.emailfield.text()
        password = self.pwdfield.text()
        password_b = self.cnfpwdfield.text()

        if len(user)==0 or len(password)==0 or len(email)==0 or len(password_b)==0:
            self.alertbox.setText("Please input all fields.")
        elif password != password_b:
            self.alertbox.setText("Passwords do not match, Try Again!")
        else:
            self.alertbox.setText(f"{user}, {email}, {password}, {password_b}") #Testing Input Fields
            # hashed_pwd = hash_engine.hash(password)
            #INSERT HASHING MODULE AND DATABASE LOGIC




# class NewAccScreen(QDialog):
#     def __init__(self):
#         super(NewAccScreen, self).__init__()
#         load_ui.loadUi("vault8_newacc.ui", self)

#         label = QLabel(self)
#         pixmap = QPixmap("Resources/vault8_login_wrapper_v0.1.png")
#         label.setPixmap(pixmap)


app = QApplication(sys.argv)
mainwindow = LoginScreen()
widget = QtWidgets.QStackedWidget()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedHeight(530)
widget.setFixedWidth(850)
widget.show()
sys.exit(app.exec())
