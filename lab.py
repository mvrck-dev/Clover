
# import sqlite3


# db = sqlite3.connect("sample.db")
# cur = db.cursor()

# tbl1_ddl = """CREATE TABLE if not exists CLOVER_MASTERDB (
#     ID INTEGER PRIMARY KEY AUTOINCREMENT,
#     CLOVER_ID TEXT UNIQUE NOT NULL,
#     CLOVER_EMAIL TEXT UNIQUE NOT NULL,
#     CLOVER_PASSWORD TEXT NOT NULL,
#     SALT TEXT NOT NULL)"""

# cur.execute(tbl1_ddl)
# # cur.execute("pragma table_info('CLOVER_MASTERDB');")
# # print(cur.fetchall())


# db.commit()

# # db.close()




















# import mysql.connector as mysql


# # Initialising Database
# activedb = mysql.connect(host = "localhost", user = "root", password= "destiny012", database = "Clover")
# print("Initialised MySql Database Connection.")
# cur = activedb.cursor()

# # Setting Up Databases
# cur.execute(f"CREATE DATABASE if not exists Clover")
# print("Database has been successfully created.")
# cur.execute("USE Clover")
# print("Database Clover is Active.")
# cur.execute(f"CREATE TABLE if not exists clover_logindb(userid int(5) PRIMARY KEY, username varchar(20) NOT NULL UNIQUE, email varchar(50) NOT NULL UNIQUE, password varchar(1000) NOT NULL);")
# print("Master Login is now active")
# # cur.execute(f"CREATE TABLE if not exists master_login_db(userid int(5), username varchar(20) NOT NULL, appname(20) NOT NULL, app_password varchar(1000) NOT NULL);")
# # print("Master Login is now active")

# #insert into master_login_db values(0001, 'ray', 'concepts.ray@gmail.com', '08ed649a54beeca6e677962ea65ce7ea20267dc0ce4a0c88b6a6d5bdf22a5e71');










































# import subprocess, sys

# try:
#     import re
#     print("re is installed")
# except ImportError:
#     print("re is not installed")
#     print("installing blender")
#     subprocess.check_call([sys.executable, "-m", "pip", "install", 're'])
#     print("re is now installed")
#     import re

# try:
#     import mysql.connector
#     print("mysql.connector is installed")
# except ImportError:
#     print("mysql.connector is not installed")
#     print("installing mysql.connector")
#     subprocess.check_call([sys.executable, "-m", "pip", "install", 'mysql.connector'])
#     print("mysql.connector is now installed")
#     import mysql.connector

# try:
#     import sqlite3
#     print("sqlite3 is installed")
# except ImportError:
#     print("sqlite3 is not installed")
#     print("installing sqlite3")
#     subprocess.check_call([sys.executable, "-m", "pip", "install", 'sqlite3'])
#     print("sqlite3 is now installed")
#     import sqlite3

# try:
#     import Crypto
#     print("pycryptodome is installed")
# except ImportError:
#     print("pycryptodome is not installed")
#     print("installing pycryptodome")
#     subprocess.check_call([sys.executable, "-m", "pip", "install", 'pycryptodome'])
#     print("pycryptodome is now installed")
#     import Crypto

# try:
#     import base64
#     print("base64 is installed")
# except ImportError:
#     print("base64 is not installed")
#     print("installing base64")
#     subprocess.check_call([sys.executable, "-m", "pip", "install", 'base64'])
#     print("base64 is now installed")
#     import base64

# try:
#     import cryptography
#     print("cryptography is installed")
# except ImportError:
#     print("cryptography is not installed")
#     print("installing cryptography")
#     subprocess.check_call([sys.executable, "-m", "pip", "install", 'cryptography'])
#     print("cryptography is now installed")
#     import cryptography

# try:
#     import hashlib
#     print("hashlib is installed")
# except ImportError:
#     print("hashlib is not installed")
#     print("installing hashlib")
#     subprocess.check_call([sys.executable, "-m", "pip", "install", 'hashlib'])
#     print("hashlib is now installed")
#     import hashlib




























































# import Crypto.Cipher.AES as AES
# from base64 import b64encode
# from Crypto.Util.Padding import pad, unpad
# from hashlib import sha256
# import hashlib
# import random
# from cryptography.fernet import Fernet


# key = Fernet.generate_key()

# # with open('key.key', 'wb') as key_file:
# #     key_file.write(key)

# with open('key.key', 'rb') as key_file:
#     key = key_file.read()

# print(key)

# f = Fernet(key)

# # with open('secrets.py', 'rb') as secret_file:
# #     secrets = secret_file.read()

# # encrypted = f.encrypt(secrets)

# # with open('enc_secrets.py', 'wb') as enc_file:
# #     enc_file.write(encrypted)
  
# with open('enc_secrets.py', 'rb') as enc_file:
#     encrypted = enc_file.read()

# decrypted = f.decrypt(encrypted)

# with open('dec_secrets.py', 'wb') as dec_file:
#     dec_file.write(decrypted)



  













#CIPHER ENCRYPTION : To generate a unique Salt for encryption
# characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '!', '_']
# def caesar_encrypt(plain_text, shift_key):
#   cipher_text = ""
#   for letter in plain_text:
#     position = characters.index(letter)
#     new_position = position + shift_key
#     cipher_text += characters[new_position]
#   # print(f"The encoded text is {cipher_text}") #Testing``
#   return cipher_text


# def caesar_decrypt(cipher_text, shift_key):
#   plain_text = ""
#   for letter in cipher_text:
#     position = characters.index(letter)
#     new_position = position - shift_key
#     plain_text += characters[new_position]
#   # print(f"The decoded text is {plain_text}")  #Testing
#   return plain_text

# #HASHING STATION
# def hash(pwd, salt):
#     hash = salt + pwd
#     hashed_string = hashlib.sha256(hash.encode('utf-8')).hexdigest()
#     return hashed_string

# #PASSWORD GENRATOR
# def pwd_generator():
#   letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
#              'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
#   numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
#   symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
#   nr_letters = 10
#   nr_symbols = 4
#   nr_numbers = 6
#   password_list = []
#   for char in range(1, nr_letters + 1):
#       password_list += random.choice(letters)
#   for char in range(1, nr_symbols + 1):
#       password_list += random.choice(symbols)
#   for char in range(1, nr_numbers + 1):
#       password_list += random.choice(numbers)
#   random.shuffle(password_list)
#   password = ''
#   for char in password_list:
#       password += char
#   return password
  
# # AES ENCRYPTION
# # def hkey(key):
# #     return hashlib.sha256(key.encode()).digest()
# # # key = f"{secrets.aes_key}"
# # hkey = sha256(key.encode()).digest()

# # def aes_encrypt(hkey, appname, app_password):
# #     presalt = caesar_encrypt(appname, 5)
# #     saltpwd = presalt + app_password

# #     cipher = AES.new(hkey, AES.MODE_ECB, )
# #     return cipher.encrypt(saltpwd)

# def aes_encrypt(key, appname, app_password):
#     hkey = bytes(hashlib.sha256(str(key).encode()).digest(), 'utf-8')
#     iv = bytes(caesar_encrypt(appname, 5), 'utf-8')
#     cipher = AES.new(hkey, AES.MODE_CBC, iv)
#     encrypted = cipher.encrypt(pad(app_password.encode("UTF-8"), AES.block_size))
#     return b64encode(encrypted).decode('utf-8')      
    

# # def aes_decrypt(hkey, appname, app_password):
# #     cipher = AES.new(hkey, AES.MODE_ECB)
# #     saltdecrtypt = cipher.decrypt(app_password)
# #     presalt = caesar_decrypt(appname, 5)
# #     orig_pwd = saltdecrtypt.replace(presalt, "")
# #     return orig_pwd
    
# def aes_decrypt(key, appname, app_password):
#     hkey = bytes(hashlib.sha256(str(key).encode()).digest(), 'utf-8')
#     iv = bytes(caesar_encrypt(appname, 5), 'utf-8')
#     cipher = AES.new(hkey, AES.MODE_CBC, iv)
#     decrypted = cipher.decrypt(pad(app_password.encode("UTF-8"), AES.block_size))
#     return b64encode(decrypted).decode('utf-8')      
    
# encrypt = aes_encrypt("key", "appname", "app_password")
# print(encrypt)




































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