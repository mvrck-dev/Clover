
from random import randbytes, random
import sys
from PyQt6.uic import loadUi
from PyQt6.QtWidgets import QApplication, QDialog, QLabel, QLineEdit, QWidget, QPushButton
from PyQt6.QtGui import QIcon, QPixmap, QFont, QFontDatabase
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6 import QtWidgets
import mysql.connector as dbcn
from hash_engine import hash

activedb = dbcn.connect(host = "localhost", user = "root", password= "destiny012", database = "Vault8")
cur = activedb.cursor()



class LoginScreen(QDialog): # Login Screen
    def __init__(self):
        super(LoginScreen, self).__init__()
        label = QLabel(self)
        pixmap = QPixmap("Resources/vault8_login_wrapper_v0.1.png")
        
        label.setPixmap(pixmap)
        loadUi("vault8_login.ui", self)

        self.loginbutton.clicked.connect(self.loginfunction)
        self.signupbutton.clicked.connect(self.gotocreate)
        

    def loginfunction(self): # This is the login function [Done!]
        user = self.usrnmfield.text()
        password = self.pwdfield.text()

        if len(user) == 0 or len(password) == 0:
            self.alertbox.setText("Please Input all Fields!")
        else:
            hashed_pwd = hash(password)
            cur.execute(f"SELECT password FROM master_login_db WHERE username = '{user}'")
            result = cur.fetchall()
            if len(result) == 0:
                self.alertbox.setText("Invalid Username!")
            elif hashed_pwd == result[0][0]:
                self.loginbutton.clicked.connect(self.gotodashboard)
            else:
                self.alertbox.setText("Invalid Password!")

    def gotocreate(self): #[WIP]
        signup = SignUpScreen()
        widget.addWidget(signup)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def gotodashboard(self): #[WIP]
        dashboard = DashboardScreen()
        widget.addWidget(dashboard)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class SignUpScreen(QDialog): # Sign Up Screen
    def __init__(self):
        super(SignUpScreen, self).__init__()
        label = QLabel(self)
        pixmap = QPixmap("Resources/vault8_login_wrapper_v0.1.png")
        label.setPixmap(pixmap)
        loadUi("vault8_signup.ui",self)

        self.signupbutton.clicked.connect(self.SignUpFunction)
        self.returnbtn.clicked.connect(self.gotologin)

    def SignUpFunction(self): # This is the sign up function [WIP!]
        user = self.usrnmfield.text()
        email = self.emailfield.text()
        password = self.pwdfield.text()
        password_b = self.cnfpwdfield.text()

        if len(user)==0 or len(password)==0 or len(email)==0 or len(password_b)==0:
            self.alertbox.setText("Please input all fields.")

        elif password != password_b:
            self.alertbox.setText("Passwords do not match, Try Again!")
        else:
            user_db = user + "_appdb"
            hashed_pwd = hash(password)
            self.alertbox.setText(f"{user_db}, {email}, {password}, {password_b}, {hashed_pwd}") #testing
            cur.execute(f"CREATE TABLE if not exists {user_db}(userid int(5), username varchar(20) NOT NULL, appname(20) NOT NULL, app_password varchar(1000) NOT NULL);")
            cur.execute(f"INSERT INTO master_login_db (username, email, password) VALUES ('{user}', '{email}', '{hashed_pwd}')")
            activedb.commit()
            self.signupbutton.clicked.connect(self.gotologin)
           #INSERT HASHING MODULE AND DATABASE LOGIC

    def gotologin(self): #[WIP]
        login = LoginScreen()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex() + 1)

class DashboardScreen(QDialog): # Dashboard Screen
    def __init__(self):
        super(DashboardScreen, self).__init__()
        
        loadUi("vault8_dashboard.ui",self)
        # Load Button Icons
        self.logoutbtn.setIcon(QIcon("Resources/logout_icon.png"))
        self.addbtn.setIcon(QIcon("Resources/add_icon.png"))
        self.removebtn.setIcon(QIcon("Resources/remove_icon.png"))

        #Load Button Functions
        self.logoutbtn.clicked.connect(self.logoutfunction) #LogOut Function

    def logoutfunction(self): #[WIP]
        login = LoginScreen()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex() - 1)


app = QApplication(sys.argv)
mainwindow = LoginScreen()
widget = QtWidgets.QStackedWidget()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedHeight(530)
widget.setFixedWidth(850)
widget.show()
sys.exit(app.exec())



# self.alertbox.setText(hashed_pwd) #Tested and working
            # cur.execute(f"SELECT password FROM login_info WHERE username ={user}")
            # result_pass = cur.fetchone()[0]
            # if db_pwd == hashed_pwd:
            #     print("Successfully logged in.")
            #     self.error.setText("")
            #     self.connect(self.dashbaord)
            
            # else:
            #     self.error.setText("Invalid username or password")