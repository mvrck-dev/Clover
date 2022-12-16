#Initialise Clover
import clover_init
clover_init.db_init()
#Import the rest of the modules
import sqlite3 as sql
import time
import sys ,os
import re
#PyQt Modules
from PyQt6.uic import loadUi
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QDialog, QLabel, QProgressBar
from PyQt6.QtGui import QIcon, QPixmap, QFont, QFontDatabase 
from PyQt6.QtCore import *
#Custom modules
import clover_cryptographer
import clover_stylesheets as styles

#Conncection to SQLite DB
activedb = sql.connect("CLOVER_DB.db")
cur = activedb.cursor()
time.sleep(2)

#Application Start
#Login Screen
class LoginScreen(QDialog): # Login Screen #AES DECRYPTION 
    def __init__(self):
        #Load the UI
        super(LoginScreen, self).__init__()
        label = QLabel(self)
        pixmap = QPixmap("rsrc/clover_login_bg_v1.png")
        label.setPixmap(pixmap)
        loadUi("clover_login.ui", self)
        #Set the window title
        self.setWindowTitle("Clover | Login")
        #Set the window icon
        self.setWindowIcon(QIcon("rsrc/clover_icon.png"))
        
        #Assign functions to buttons
        self.loginbutton.clicked.connect(self.loginfunction)
        self.signupbutton.clicked.connect(self.gotocreate)

        #UI Styling
        self.loginbutton.setStyleSheet(styles.button_style)
        self.signupbutton.setStyleSheet(styles.button_style)
        self.usrnmfield.setStyleSheet(styles.form_style)
        self.pwdfield.setStyleSheet(styles.form_style)

    #Login Function
    def loginfunction(self):
        global user #global variable for the user
        user = self.usrnmfield.text().lower() #Get the username
        password = self.pwdfield.text() #Get the password
        #Check if the username exists
        cur.execute(f"SELECT COUNT(CLOVER_USRNM) FROM CLOVER_MASTERDB WHERE CLOVER_USRNM = '{user}'")
        row_count = cur.fetchall()
        def login():
            if len(user) == 0 or len(password) == 0: #Check if the fields are empty
                self.alertbox.setText("Please Input all Fields!")
                timer.singleShot(2000, self.clear_alertbox)
            elif row_count[0][0] == 0: #Check if the username exists
                self.alertbox.setText("Login Credentials Not Found.\nPlease Create an Account First!")
                timer.singleShot(2000, self.clear_alertbox)
            else: 
                #Check if the password is correct
                cur.execute(f"SELECT nKEY FROM CLOVER_MASTERDB WHERE CLOVER_USRNM = '{user}' or CLOVER_EMAIL = '{user}'")
                special_key = cur.fetchone()
                hashed_pwd = clover_cryptographer.hash(password, special_key[0])
                cur.execute(f"SELECT CLOVER_PWD FROM CLOVER_MASTERDB WHERE CLOVER_USRNM = '{user}' or CLOVER_EMAIL = '{user}'")
                result = cur.fetchall()
                if len(result) == 0: 
                    self.alertbox.setText("Invalid Username or Email!")
                    timer.singleShot(2000, self.clear_alertbox)
                elif hashed_pwd == result[0][0]: #If the password is correct
                    self.alertbox.setText("Authenticated!\nPress Login again to continue.")
                    timer.singleShot(2000, self.clear_alertbox)
                    self.loginbutton.clicked.connect(self.gotodashboard)
                else: #If the password is incorrect
                    self.alertbox.setText("Invalid Password!")
                    timer.singleShot(2000, self.clear_alertbox)
        login() #Call the login function


    def gotocreate(self): #signup page link
        signup = SignUpScreen()
        widget.addWidget(signup)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def gotodashboard(self): #dashboard page link
        dashboard = DashboardScreen()
        widget.addWidget(dashboard)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def clear_alertbox(self):
        self.alertbox.setText("")


#Signup Screen
class SignUpScreen(QDialog): # Sign Up Screen 
    def __init__(self):
        super(SignUpScreen, self).__init__()
        label = QLabel(self)
        pixmap = QPixmap("rsrc/clover_login_bg_v2.png")
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
        
    def SignUpFunction(self): # This is the sign up function 
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
            salt = clover_cryptographer.caesar_encrypt(user, 8)
            hashed_pwd = clover_cryptographer.hash(password, salt)
            self.alertbox.setText(f"{user_db}, {email}, {password}, {password_b}, {hashed_pwd}") #testing
            cur.execute(f"CREATE TABLE if not exists {user_db}(email varchar(50), appname varchar(20) NOT NULL, app_password varchar(100) NOT NULL);")
            cur.execute(f"INSERT INTO CLOVER_MASTERDB(CLOVER_USRNM, CLOVER_EMAIL, CLOVER_PWD, nKEY) VALUES('{user}','{email}', '{hashed_pwd}', '{salt}')")
            activedb.commit()
            self.alertbox.setText("Account Created Successfully!\nRedirecting to Login Screen...")
            timer.singleShot(1000, self.gotologin)


    def gotologin(self):
        login = LoginScreen()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def clear_alertbox(self):
        self.alertbox.setText("")



class DashboardScreen(QDialog): # Dashboard Screen 
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
            app_password = clover_cryptographer.pwd_generator()
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
            app_password = clover_cryptographer.pwd_generator()
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
    def remove_app(self): 
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