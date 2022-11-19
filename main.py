import sys ,os
from PyQt6.uic import loadUi
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QDialog, QLabel, QSplashScreen
from PyQt6.QtGui import QIcon, QPixmap, QFont, QFontDatabase 
from PyQt6.QtCore import *
import re
import mysql.connector as mysql
import cipher_module
import vault8_stylesheets as styles
import sqlite3 as sql
import time


# activedb = mysql.connect(host = "localhost", user = "root", password= "destiny012", database = "Vault8")
# cur = activedb.cursor(buffered=True)
activedb = sql.connect("CLOVER_DB.db")
cur = activedb.cursor()


tbl1_ddl = """CREATE TABLE if not exists CLOVER_MASTERDB (
    SERIAL_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    CLOVER_USRNM TEXT UNIQUE NOT NULL,
    CLOVER_EMAIL TEXT UNIQUE NOT NULL,
    CLOVER_PWD TEXT NOT NULL,
    nKEY TEXT NOT NULL)"""
cur.execute(tbl1_ddl)


# class SplashScreen(QSplashScreen):
#     def __init__(self):
#         super(SplashScreen, self).__init__()
#         loadUi("CLOVER_splash.ui", self)
#         # self.setWindowIcon(QIcon("vault8.ico"))
#         self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
#         self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
#         # self.show()
#         # self.timer = QTimer()
#         # self.timer.timeout.connect(self.progress)
#         # self.timer.start(35)
#         # self.progressbar.setValue(0)

#     def progress(self):
#         for i in range(100):
#             time.sleep(0.01)
#             self.progressbar.setValue(i + 1)

#         # global progress
#         # progress = self.progressbar.value()
#         # progress += 1
#         # self.progressbar.setValue(progress)
#         # if progress > 100:
#         #     self.timer.stop()
#         #     self.main = Login()
#         #     self.main.show()
#         #     self.close()

#     # def mousePressEvent(self, event):
#     #     self.dragPos = event.globalPos()

#     # def mouseMoveEvent(self, event):
#     #     if event.buttons() == Qt.MouseButton.LeftButton:
#     #         self.move(self.pos() + event.globalPos() - self.dragPos)
#     #         self.dragPos = event.globalPos()
#     #         event.accept()



class LoginScreen(QDialog): # Login Screen #AES DECRYPTION 
    def __init__(self):
        super(LoginScreen, self).__init__()
        label = QLabel(self)
        pixmap = QPixmap("rsrc/clover_login_bg_v1.png")
        
        label.setPixmap(pixmap)
        loadUi("clover_login.ui", self)

        self.loginbutton.clicked.connect(self.loginfunction)
        self.signupbutton.clicked.connect(self.gotocreate)

        #UI Styling
        self.loginbutton.setStyleSheet(styles.button_style)
        self.signupbutton.setStyleSheet(styles.button_style)
        self.usrnmfield.setStyleSheet(styles.form_style)
        self.pwdfield.setStyleSheet(styles.form_style)

    def loginfunction(self):
        global user #global variable for the user
        user = self.usrnmfield.text().lower()
        password = self.pwdfield.text()
        cur.execute(f"SELECT COUNT(CLOVER_USRNM) FROM CLOVER_MASTERDB WHERE CLOVER_USRNM = '{user}'")
        row_count = cur.fetchall()
        def login():
            if len(user) == 0 or len(password) == 0:
                self.alertbox.setText("Please Input all Fields!")
                timer.singleShot(2000, self.clear_alertbox)
            elif row_count[0][0] == 0:
                self.alertbox.setText("Login Credentials Not Found.\nPlease Create an Account First!")
                timer.singleShot(2000, self.clear_alertbox)
            else:
                cur.execute(f"SELECT nKEY FROM CLOVER_MASTERDB WHERE CLOVER_USRNM = '{user}' or CLOVER_EMAIL = '{user}'")
                special_key = cur.fetchone()
                hashed_pwd = cipher_module.hash(password, special_key[0])
                cur.execute(f"SELECT CLOVER_PWD FROM CLOVER_MASTERDB WHERE CLOVER_USRNM = '{user}' or CLOVER_EMAIL = '{user}'")
                result = cur.fetchall()
                if len(result) == 0:
                    self.alertbox.setText("Invalid Username or Email!")
                    timer.singleShot(2000, self.clear_alertbox)
                elif hashed_pwd == result[0][0]:
                    self.alertbox.setText("Authenticated!\nPress Login again to continue.")
                    timer.singleShot(5000, self.clear_alertbox)
                    self.loginbutton.clicked.connect(self.gotodashboard)
                else:
                    self.alertbox.setText("Invalid Password!")
                    timer.singleShot(2000, self.clear_alertbox)
        login()

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


#THERE ARE STILL BUGS IN THE FLOW OF THE CODE OF THIS MF! I NEED TO FIX IT ASAP!
class SignUpScreen(QDialog): # Sign Up Screen #FIX SPECIAL CHARACTERS ENTRY ISSUE and password strength checker and aes encrption
    def __init__(self):
        super(SignUpScreen, self).__init__()
        label = QLabel(self)
        pixmap = QPixmap("rsrc/clover_login_bg_v1.png")
        label.setPixmap(pixmap)
        loadUi("clover_signup.ui",self)
        
        #Assiging Functions to buttons
        self.returnbtn.clicked.connect(self.gotologin)
        self.signupbutton.clicked.connect(self.SignUpFunction)
        
        #UI Styling
        self.returnbtn.setIcon(QIcon("rsrc/return_icon.png"))
        self.signupbutton.setStyleSheet(styles.button_style)
        self.usrnmfield.setStyleSheet(styles.form_style)
        self.pwdfield.setStyleSheet(styles.form_style)
        self.emailfield.setStyleSheet(styles.form_style)
        self.cnfpwdfield.setStyleSheet(styles.form_style)
        
    def SignUpFunction(self): # This is the sign up function [WIP!]
        user = self.usrnmfield.text().lower()
        email = self.emailfield.text().lower()
        password = self.pwdfield.text()
        password_b = self.cnfpwdfield.text()

        cur.execute(f"SELECT count(CLOVER_USRNM) FROM CLOVER_MASTERDB WHERE CLOVER_USRNM = '{user}'")
        checkUser = cur.fetchall()
        cur.execute(f"SELECT count(CLOVER_EMAIL) FROM CLOVER_MASTERDB WHERE CLOVER_EMAIL = '{email}'")
        checkEmail = cur.fetchall()

        if len(user)==0 or len(password)==0 or len(email)==0 or len(password_b)==0:
            self.alertbox.setText("Please input all fields.")
            timer.singleShot(2000, self.clear_alertbox)

        elif (re.fullmatch(regex, email)) == None:
            self.alertbox.setText("Please input a valid email.")
            timer.singleShot(2000, self.clear_alertbox)

        elif password != password_b:
            self.alertbox.setText("Passwords do not match, Try Again!")
            timer.singleShot(2000, self.clear_alertbox)
            
        elif len(password) < 8:
            self.alertbox.setText("Password must be atleast 8 characters long!")
            timer.singleShot(2000, self.clear_alertbox)

        elif checkUser == [(1,)]:
            self.alertbox.setText("Username already exists! Try another one.")
            timer.singleShot(2000, self.clear_alertbox)
        
        elif checkEmail == [(1,)]:
            self.alertbox.setText("Email already exists! Try another one.")
            timer.singleShot(2000, self.clear_alertbox)

        else:
            user_db = user + "_clover_appdb"
            salt = cipher_module.caesar_encrypt(user, 8)
            hashed_pwd = cipher_module.hash(password, salt)
            self.alertbox.setText(f"{user_db}, {email}, {password}, {password_b}, {hashed_pwd}") #testing
            cur.execute(f"CREATE TABLE if not exists {user_db}(email varchar(50), appname varchar(20) NOT NULL, app_password varchar(100) NOT NULL, app_enKEY varchar(100) NOT NULL);")
            cur.execute(f"INSERT INTO CLOVER_MASTERDB(CLOVER_USRNM, CLOVER_EMAIL, CLOVER_PWD, nKEY) VALUES('{user}','{email}', '{hashed_pwd}', '{salt}')")
            activedb.commit()
            self.alertbox.setText("Account Created Successfully!\nRedirecting to Login Screen...")
            timer.singleShot(2200, self.gotologin)

    def gotologin(self):
        login = LoginScreen()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def clear_alertbox(self):
        self.alertbox.setText("")



class DashboardScreen(QDialog): # Dashboard Screen | AND ADD DATABASE TO LIST
    def __init__(self):
        super(DashboardScreen, self).__init__()
        label = QLabel(self)
        pixmap = QPixmap("rsrc/dashboard_art.png")
        label.setPixmap(pixmap)
        loadUi("clover_dashboard.ui",self)

        #Load Button Functions
        self.logoutbtn.clicked.connect(self.logoutfunction) #LogOut Function
        self.addbtn.clicked.connect(self.add_app) #Add App Function
        self.removebtn.clicked.connect(self.remove_app) #Remove App Function
        self.applist.clicked.connect(self.display_details) #App Display Function
        self.generatepwd.clicked.connect(self.generate_password) #Generate Password Function
        self.copypwd.clicked.connect(self.CtCpwd) #Copy to Clipboard Function
        
        # Load Button Icons
        self.logoutbtn.setIcon(QIcon("rsrc/logout_icon.png"))
        self.addbtn.setIcon(QIcon("rsrc/add_icon.png"))
        self.removebtn.setIcon(QIcon("rsrc/remove_icon.png"))
        #UI Styling
        self.cbody.setStyleSheet("background-color: #0c0d0c;")
        self.usrnm.setStyleSheet("color: #FFFFFF; font-size: 30px; font-weight: 200;")
        self.applist.setStyleSheet(styles.list_style)
        self.appfield.setStyleSheet(styles.form_style2)
        self.emailfield.setStyleSheet(styles.form_style2)
        self.generatepwd.setStyleSheet(styles.button_style2)
        self.copypwd.setStyleSheet(styles.button_style2)
        self.addbtn.setStyleSheet(styles.button_style2)
        self.appname.setStyleSheet(styles.block_style)
        self.emailid.setStyleSheet(styles.block_style)
        self.logoutbtn.setStyleSheet(styles.logout_button)
        


        global active_user
        active_user = user
        self.usrnm.setText(active_user)

        #Load App List
        self.applist.clear()
        cur.execute(f"SELECT appname FROM {active_user}_clover_appdb")
        app_list = cur.fetchall()
        for app in app_list:
            self.applist.addItem(app[0])
        
    #Add items to list
    def add_app(self):
        if len(self.appfield.text()) == 0:
            self.alertbox.setText("Please input an app name!")
            self.alertbox.setStyleSheet(styles.alert)
            timer.singleShot(2000, self.clear_alertbox)
        elif len(self.emailfield.text()) == 0:
            self.alertbox.setText("Please input an email!")
            self.alertbox.setStyleSheet(styles.alert)
            timer.singleShot(2000, self.clear_alertbox)
        elif (re.fullmatch(regex, self.emailfield.text())) == None:
            self.alertbox.setText("Please input a valid email.")
            self.alertbox.setStyleSheet(styles.alert)
            timer.singleShot(2000, self.clear_alertbox)
        else:
            app_name = self.appfield.text()
            self.applist.addItem(app_name)
            app_email = self.emailfield.text()
            app_password = cipher_module.pwd_generator()
            cur.execute(f"INSERT INTO {active_user}_clover_appdb(appname, email, app_password) VALUES('{app_name}', '{app_email}', '{app_password}')")
            activedb.commit()
            self.appfield.setText("")
            self.emailfield.setText("")
            self.alertbox.setText("App Added!")
            self.alertbox.setStyleSheet(styles.success)
            timer.singleShot(2000, self.clear_alertbox)

    def generate_password(self):
        if self.applist.currentItem() == None:
            self.alertbox.setText("Please select an app!")
            self.alertbox.setStyleSheet(styles.alert)
            timer.singleShot(2000, self.clear_alertbox)
        else:
            app_name = self.applist.currentItem().text()
            #Generate Password
            app_password = cipher_module.pwd_generator()
            #Add to DB
            cur.execute(f"UPDATE {active_user}_clover_appdb SET app_password = '{app_password}' WHERE appname = '{app_name}'")
            activedb.commit()
            #Copy to Clipboard
            cb = QApplication.clipboard()
            cb.clear()
            cb.setText(app_password)
            self.alertbox.setText("Password Generated and Copied!")  
            self.alertbox.setStyleSheet(styles.success)
            timer.singleShot(2000, self.clear_alertbox)

    def CtCpwd(self):
        while self.applist.currentItem() == None:
            self.alertbox.setText("Please select an app!")
            self.alertbox.setStyleSheet(styles.alert)
            timer.singleShot(2000, self.clear_alertbox)
            break
        else:
            #Copy to Clipboard
            app_name = self.applist.currentItem().text()
            cb = QApplication.clipboard()
            cb.clear()
            cur.execute(f"SELECT app_password FROM {active_user}_clover_appdb WHERE appname = '{app_name}'")
            app_password = cur.fetchone()[0]
            cb.setText(app_password)
            self.alertbox.setText("Password Copied to Clipboard!")
            timer.singleShot(2000, self.clear_alertbox)
            self.alertbox.setStyleSheet(styles.success)


    #Remove items from list
    def remove_app(self): #DONE
        while self.applist.currentItem() == None:
            self.alertbox.setText("Please select an app!")
            self.alertbox.setStyleSheet(styles.alert)
            timer.singleShot(2000, self.clear_alertbox)
            break
        else:
            app_name = self.applist.currentRow()
            app_item = self.applist.currentItem().text()
            self.applist.takeItem(app_name)
            self.appname.setText("")
            cur.execute(f"DELETE FROM {active_user}_clover_appdb WHERE appname = '{app_item}'")
            activedb.commit()
            self.alertbox.setText("App Removed!")
            self.alertbox.setStyleSheet(styles.success)

    #Display App Data
    def display_details(self):
        while self.applist.currentItem() != None:
            app_name = self.applist.currentItem().text()
            cur.execute(f"SELECT email FROM {active_user}_clover_appdb WHERE appname = '{app_name}'")
            email = cur.fetchone()[0]
            self.appname.setText(app_name)
            self.emailid.setText(email)
            break

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
widget.setFixedWidth(930)
widget.setFixedHeight(500)
widget.show()

#Font
ROOT_DIR = os.path.realpath(os.path.join(os.path.dirname(__file__), '.'))
ffl = os.path.join(ROOT_DIR, 'rsrc', 'Gilroy.ttf')
id = QFontDatabase.addApplicationFont(ffl)
families = QFontDatabase.applicationFontFamilies(id)
current_font = families[0]
app.setFont(QFont(current_font, 10))
#Misceallaneous
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
timer = QTimer()

sys.exit(app.exec())

#abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+~`|}{[]\:;?><,./-=