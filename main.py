
from random import randbytes, random
import sys
from PyQt6.uic import loadUi
from PyQt6.QtWidgets import QApplication, QDialog, QLabel, QLineEdit, QWidget, QPushButton
from PyQt6.QtGui import QIcon, QPixmap, QFont, QFontDatabase, QGuiApplication
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6 import QtWidgets
import re
import mysql.connector as dbcn
import cipher_module




activedb = dbcn.connect(host = "localhost", user = "root", password= "destiny012", database = "Vault8")
cur = activedb.cursor(buffered=True)



class LoginScreen(QDialog): # Login Screen #AES DECRYPTION
    def __init__(self):
        super(LoginScreen, self).__init__()
        label = QLabel(self)
        pixmap = QPixmap("rsrc/vault8_login_wrapper_v0.1.png")
        
        label.setPixmap(pixmap)
        loadUi("vault8_login.ui", self)

        self.loginbutton.clicked.connect(self.loginfunction)
        self.signupbutton.clicked.connect(self.gotocreate)

    def loginfunction(self):
        global user #global variable for the user
        user = self.usrnmfield.text()
        password = self.pwdfield.text()
        cur.execute("SELECT * FROM master_login_db WHERE username = %s AND password = %s", (user, password))

        if len(user) == 0 or len(password) == 0:
            self.alertbox.setText("Please Input all Fields!")
            timer.singleShot(3000, self.clear_alertbox)
        else:
            cur.execute(f"SELECT special_key FROM master_login_db WHERE username = '{user}' or email = '{user}'")
            special_key = cur.fetchone()
            hashed_pwd = cipher_module.hash(password, special_key[0])
            cur.execute(f"SELECT password FROM master_login_db WHERE username = '{user}' or email = '{user}'")
            result = cur.fetchall()
            if len(result) == 0:
                self.alertbox.setText("Invalid Username or Email!")
                timer.singleShot(3000, self.clear_alertbox)
            elif hashed_pwd == result[0][0]:
                self.alertbox.setText("Authenticated!\nPress Login again to continue.")
                timer.singleShot(5000, self.clear_alertbox)
                self.loginbutton.clicked.connect(self.gotodashboard)
            else:
                self.alertbox.setText("Invalid Password!")
                timer.singleShot(3000, self.clear_alertbox)

    def gotocreate(self): #[WIP]
        signup = SignUpScreen()
        widget.addWidget(signup)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def gotodashboard(self): #[WIP]
        dashboard = DashboardScreen()
        widget.addWidget(dashboard)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def clear_alertbox(self):
        self.alertbox.setText("")
        self.alertbox.setStyleSheet("background-color: #00000000; color: #00000000;")


#THERE ARE STILL BUS IN THE FLOW OF THE CODE OF THIS MF! I NEED TO FIX IT ASAP!
class SignUpScreen(QDialog): # Sign Up Screen #FIX SPECIAL CHARACTERS ENTRY ISSUE and password strength checker and aes encrption
    def __init__(self):
        super(SignUpScreen, self).__init__()
        label = QLabel(self)
        pixmap = QPixmap("rsrc/vault8_login_wrapper_v0.1.png")
        label.setPixmap(pixmap)
        loadUi("vault8_signup.ui",self)
        
        #Styling
        self.returnbtn.setIcon(QIcon("rsrc/return_icon.png"))

        #Assiging Functions to buttons
        self.returnbtn.clicked.connect(self.gotologin)
        self.signupbutton.clicked.connect(self.SignUpFunction)


    def SignUpFunction(self): # This is the sign up function [WIP!]
        user = self.usrnmfield.text()
        email = self.emailfield.text()
        password = self.pwdfield.text()
        password_b = self.cnfpwdfield.text()

        cur.execute(f"SELECT count(username) FROM master_login_db WHERE username = '{user}'")
        checkUser = cur.fetchall()


        if len(user)==0 or len(password)==0 or len(email)==0 or len(password_b)==0:
            self.alertbox.setText("Please input all fields.")
            timer.singleShot(3000, self.clear_alertbox)

        elif (re.fullmatch(regex, email)) == None:
            self.alertbox.setText("Please input a valid email.")
            timer.singleShot(3000, self.clear_alertbox)

        elif password != password_b:
            self.alertbox.setText("Passwords do not match, Try Again!")
            timer.singleShot(3000, self.clear_alertbox)
            
        elif len(password) < 8:
            self.alertbox.setText("Password must be atleast 8 characters long!")
            timer.singleShot(3000, self.clear_alertbox)

        elif checkUser == [(1,)]:
            self.alertbox.setText("Username already exists! Try another one.")
            timer.singleShot(3000, self.clear_alertbox)

        else:
            user_db = user + "_appdb"
            salt = cipher_module.caesar_encrypt(user, 8)
            hashed_pwd = cipher_module.hash(password, salt)
            self.alertbox.setText(f"{user_db}, {email}, {password}, {password_b}, {hashed_pwd}") #testing
            cur.execute(f"CREATE TABLE if not exists {user_db}(email varchar(50), appname varchar(20) NOT NULL, app_password varchar(100) NOT NULL);")
            cur.execute(f"INSERT INTO master_login_db(username, email, password, special_key) VALUES('{user}','{email}', '{hashed_pwd}', '{salt}')")
            activedb.commit()
            self.alertbox.setText("Account Created Successfully!\nRedirecting to Login Screen...")
            timer.singleShot(2200, self.gotologin)

    def gotologin(self):
        login = LoginScreen()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def clear_alertbox(self):
        self.alertbox.setText("")
        self.alertbox.setStyleSheet("background-color: #00000000; color: #00000000;")



class DashboardScreen(QDialog): # Dashboard Screen | AND ADD DATABASE TO LIST
    def __init__(self):
        super(DashboardScreen, self).__init__()
        loadUi("vault8_dashboard.ui",self)
        # Load Button Icons
        self.logoutbtn.setIcon(QIcon("rsrc/logout_icon.png"))
        self.addbtn.setIcon(QIcon("rsrc/add_icon.png"))
        self.removebtn.setIcon(QIcon("rsrc/remove_icon.png"))

        #Load Button Functions
        self.logoutbtn.clicked.connect(self.logoutfunction) #LogOut Function
        self.addbtn.clicked.connect(self.add_app) #Add App Function
        self.removebtn.clicked.connect(self.remove_app) #Remove App Function
        self.applist.clicked.connect(self.display_app) #App Clicked Function
        self.generatepwd.clicked.connect(self.generate_password) #Generate Password Function
        self.copypwd.clicked.connect(self.CtCpwd) #Copy to Clipboard Function
        
        global active_user
        active_user = user
        self.usrnm.setText(active_user)

        #Load App List
        self.applist.clear()
        cur.execute(f"SELECT appname FROM {active_user}_appdb")
        app_list = cur.fetchall()
        for app in app_list:
            self.applist.addItem(app[0])
        
    #Add items to list
    def add_app(self):
        if len(self.appfield.text()) == 0:
            self.alertbox.setText("Please input an app name!")
            self.alertbox.setStyleSheet(alert)
            timer.singleShot(3000, self.clear_alertbox)
        elif len(self.emailfield.text()) == 0:
            self.alertbox.setText("Please input an email!")
            self.alertbox.setStyleSheet(alert)
            timer.singleShot(3000, self.clear_alertbox)
        elif (re.fullmatch(regex, self.emailfield.text())) == None:
            self.alertbox.setText("Please input a valid email.")
            self.alertbox.setStyleSheet(alert)
            timer.singleShot(3000, self.clear_alertbox)
        else:
            app_name = self.appfield.text()
            self.applist.addItem(app_name)
            app_email = self.emailfield.text()
            app_password = cipher_module.pwd_generator()
            cur.execute(f"INSERT INTO {active_user}_appdb(appname, email, app_password) VALUES('{app_name}', '{app_email}', '{app_password}')")
            activedb.commit()
            self.appfield.setText("")
            self.emailfield.setText("")
            self.alertbox.setText("App Added!")
            self.alertbox.setStyleSheet(success)
            timer.singleShot(3000, self.clear_alertbox)

    def generate_password(self):
        if self.applist.currentItem() == None:
            self.alertbox.setText("Please select an app!")
            self.alertbox.setStyleSheet(alert)
            timer.singleShot(3000, self.clear_alertbox)
        else:
            app_name = self.applist.currentItem().text()
            #Generate Password
            app_password = cipher_module.pwd_generator()
            #Add to DB
            cur.execute(f"UPDATE {active_user}_appdb SET app_password = '{app_password}' WHERE appname = '{app_name}'")
            activedb.commit()
            #Copy to Clipboard
            cb = QApplication.clipboard()
            cb.clear()
            cb.setText(app_password)
            self.alertbox.setText("Password Generated and Copied!")  
            self.alertbox.setStyleSheet(success)
            timer.singleShot(3000, self.clear_alertbox)

    def CtCpwd(self):
        if self.applist.currentItem() == None:
            self.alertbox.setText("Please select an app!")
            self.alertbox.setStyleSheet(alert)
            timer.singleShot(3000, self.clear_alertbox)
        else:
            #Copy to Clipboard
            app_name = self.applist.currentItem().text()
            cb = QApplication.clipboard()
            cb.clear()
            cur.execute(f"SELECT app_password FROM {active_user}_appdb WHERE appname = '{app_name}'")
            app_password = cur.fetchone()[0]
            cb.setText(app_password)
            self.alertbox.setText("Password Copied to Clipboard!")
            self.alertbox.setStyleSheet(success)

    #Remove items from list
    def remove_app(self): #DONE
        if self.applist.currentItem() == None:
            self.alertbox.setText("Please select an app!")
            self.alertbox.setStyleSheet(alert)
            timer.singleShot(3000, self.clear_alertbox)
        else:
            app_name = self.applist.currentRow()
            app_item = self.applist.currentItem().text()
            self.applist.takeItem(app_name)
            self.appname.setText("")
            cur.execute(f"DELETE FROM {active_user}_appdb WHERE appname = '{app_item}'")
            activedb.commit()
            self.alertbox.setText("App Removed!")
            self.alertbox.setStyleSheet(success)

    #Display App Data
    def display_app(self):
        self.appname.setText(self.applist.currentItem().text())

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
#Styles for Alert Box
alert = "background-color: #ff4747; color: #ffffff;border: 0.1px; border-radius:16px;"
success = "background-color: #E4FFDF; color: #0F462D; border-radius:16px"



#Miscellaneous
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

timer = QTimer()
sys.exit(app.exec())