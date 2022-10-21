
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
import time


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
        
        #Styling
        self.returnbtn.setIcon(QIcon("Resources/return_icon.png"))

        #Assiging Functions to buttons
        self.returnbtn.clicked.connect(self.gotologin)
        self.signupbutton.clicked.connect(self.SignUpFunction)

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
            cur.execute(f"CREATE TABLE if not exists {user_db}(username varchar(20) NOT NULL, appname varchar(20) NOT NULL, app_password varchar(1000) NOT NULL);")
            cur.execute(f"INSERT INTO master_login_db (username, email, password) VALUES ('{user}', '{email}', '{hashed_pwd}')")
            activedb.commit()
            # timer.singleShot(3000, self.clear_alertbox)
            dashboard = DashboardScreen()
            widget.addWidget(dashboard)
            widget.setCurrentIndex(widget.currentIndex() + 1)



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
        self.addbtn.clicked.connect(self.add_app) #Add App Function
        self.removebtn.clicked.connect(self.remove_app) #Remove App Function
        self.applist.clicked.connect(self.display_app) #App Clicked Function
        self.generatepwd.clicked.connect(self.generate_password) #Generate Password Function
        self.copypwd.clicked.connect(self.CtCpwd) #Copy to Clipboard Function

    #Add items to list
    def add_app(self):
        if len(self.appfield.text()) == 0:
            self.alertbox.setText("Please input an app name!")
            self.alertbox.setStyleSheet("background-color: #ff4747; color: #ffffff;border: 0.1px; border-radius:16px;")
            timer.singleShot(3000, self.clear_alertbox)
        else:
            app_name = self.appfield.text()
            self.applist.addItem(app_name)
            self.appfield.setText("")
            self.alertbox.setText("App Added!")
            self.alertbox.setStyleSheet("background-color: #E4FFDF; color: #0F462D; border-radius:16px")
            timer.singleShot(3000, self.clear_alertbox)

    def generate_password(self):
        if self.applist.currentItem() == None:
            self.alertbox.setText("Please select an app!")
            self.alertbox.setStyleSheet("background-color: #ff4747; color: #ffffff;border: 0.1px; border-radius:16px;")
            timer.singleShot(3000, self.clear_alertbox)
        else:
            app_name = self.applist.currentItem().text()
            #Generate Password

            self.alertbox.setText("Password Generated!")    

    def CtCpwd(self):
        if self.applist.currentItem() == None:
            self.alertbox.setText("Please select an app!")
            self.alertbox.setStyleSheet("background-color: #ff4747; color: #ffffff;border: 0.1px; border-radius:16px;")
            timer.singleShot(3000, self.clear_alertbox)
        else:
            app_name = self.applist.currentItem().text()
            #Copy to Clipboard

            self.alertbox.setText("Password Copied to Clipboard!")

    #Remove items from list
    def remove_app(self):
        self.applist.takeItem(self.applist.currentRow())
        self.appname.setText("")

    #Display App Data
    def display_app(self):
        self.appname.setText(self.applist.currentItem().text())

    #Welcome Message
    #Username Display



    #Clear Alert Box
    def clear_alertbox(self):
        self.alertbox.setText("")
        self.alertbox.setStyleSheet("background-color: #00000000; color: #000000;")
        
    #LogOut Function
    def logoutfunction(self): #[WIP]
        login = LoginScreen()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex() + 1)



app = QApplication(sys.argv)
mainwindow = LoginScreen()
widget = QtWidgets.QStackedWidget()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedHeight(530)
widget.setFixedWidth(850)
widget.show()
timer = QTimer()
sys.exit(app.exec())