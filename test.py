import mysql.connector as mysql

activedb = mysql.connect(host = "localhost", user = "root", password= "destiny012", database = "Vault8")
cur = activedb.cursor(buffered=True)

active_user = "robin"
appname = "Git"

cur.execute(f"SELECT email FROM {active_user}_appdb WHERE appname = '{appname}'")
email = cur.fetchone()[0]
print(email)









































# from PyQt6.QtWidgets import QApplication, QWidget, QLabel
# from PyQt6.QtGui import QFont, QFontDatabase
# import sys, os
 
# class Window(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.resize(600, 300)
#         self.setWindowTitle("CodersLegacy")
#         self.setContentsMargins(20, 20, 20, 20)

#         ROOT_DIR = os.path.realpath(os.path.join(os.path.dirname(__file__), '.'))
#         print(ROOT_DIR)
#         ffl = os.path.join(ROOT_DIR, 'rsrc', 'ITCAvantGardeStd.ttf')
#         id = QFontDatabase.addApplicationFont(ffl)
#         if id == -1:
#             print("font not found", id)
#         else:
#             print("font found", id)
 
#         families = QFontDatabase.applicationFontFamilies(id)
#         print(families[0])
 
#         label = QLabel("Hello World", self)
#         label.setFont(QFont(families[0], 80))
#         label.move(50, 100)
 
# app = QApplication(sys.argv)
# window = Window()
# window.show()
# sys.exit(app.exec())



# # import os
# # ROOT_DIR = os.path.realpath(os.path.join(os.path.dirname(__file__), '.'))
# # print(ROOT_DIR)
# # file= os.path.join(ROOT_DIR, 'rsrc', 'ITCAvantGardeStd.ttf')
# # print(file)