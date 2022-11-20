import sqlite3 as sql
import subprocess
import sys
from uuid import getnode as get_mac

def package_init():
    div = 100/10
    print("Checking Packages")
    try:
        import PyQt5
        print("PyQt5 is installed")
        n = div
    except ImportError:
        print("PyQt5 is not installed")
        print("installing PyQt5")
        subprocess.check_call([sys.executable, "-m", "pip", "install", 'PyQt5'])
        subprocess.check_call([sys.executable, "-m", "pip", "install", 'pyqt5-tools'])
        print("PyQt5 is now installed")
        import PyQt5
        n += div
    try:
        import re
        print("re is installed")
        n += div
    except ImportError:
        print("re is not installed")
        print("installing re")
        subprocess.check_call([sys.executable, "-m", "pip", "install", 're'])
        print("re is now installed")
        import re
        n += div
    try:
        import uuid
        print("uuid is installed")
        n += div
    except ImportError:
        print("uuid is not installed")
        print("installing uuid")
        subprocess.check_call([sys.executable, "-m", "pip", "install", 'uuid'])
        print("uuid is now installed")
        import uuid
        n += div
    try:
        import subprocess
        print("subprocess is installed")
        n += div
    except ImportError:
        print("subprocess is not installed")
        print("installing subprocess")
        subprocess.check_call([sys.executable, "-m", "pip", "install", 'uuid'])
        print("subprocess is now installed")
        import subprocess
        n += div
    try:
        import mysql.connector
        print("mysql.connector is installed")
        n += div
    except ImportError:
        print("mysql.connector is not installed")
        print("installing mysql.connector")
        subprocess.check_call(
            [sys.executable, "-m", "pip", "install", 'mysql.connector'])
        print("mysql.connector is now installed")
        import mysql.connector
        n += div

    try:
        import sqlite3
        print("sqlite3 is installed")
        n += div
    except ImportError:
        print("sqlite3 is not installed")
        print("installing sqlite3")
        subprocess.check_call(
            [sys.executable, "-m", "pip", "install", 'sqlite3'])
        print("sqlite3 is now installed")
        import sqlite3
        n += div

    try:
        import Crypto
        print("pycryptodome is installed")
        n += div
    except ImportError:
        print("pycryptodome is not installed")
        print("installing pycryptodome")
        subprocess.check_call(
            [sys.executable, "-m", "pip", "install", 'pycryptodome'])
        print("pycryptodome is now installed")
        import Crypto
        n += div

    try:
        import base64
        print("base64 is installed")
        n += div
    except ImportError:
        print("base64 is not installed")
        print("installing base64")
        subprocess.check_call(
            [sys.executable, "-m", "pip", "install", 'base64'])
        print("base64 is now installed")
        import base64
        n += div

    try:
        import cryptography
        print("cryptography is installed")
        n += div
    except ImportError:
        print("cryptography is not installed")
        print("installing cryptography")
        subprocess.check_call(
            [sys.executable, "-m", "pip", "install", 'cryptography'])
        print("cryptography is now installed")
        import cryptography
        n += div

    try:
        import hashlib
        print("hashlib is installed")
        n += div
    except ImportError:
        print("hashlib is not installed")
        print("installing hashlib")
        subprocess.check_call(
            [sys.executable, "-m", "pip", "install", 'hashlib'])
        print("hashlib is now installed")
        import hashlib
        n += div
    return n
if package_init() >= 100:
    print(package_init())
    print("All packages are installed")
else:
    print(package_init())
    print("Some packages are not installed")
    print("Please install the missing packages")
    print("Then restart the program")


activedb = sql.connect("CLOVER_DB.db")
cur = activedb.cursor()


tbl1_ddl = """CREATE TABLE if not exists CLOVER_MASTERDB (
    SERIAL_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    CLOVER_USRNM TEXT UNIQUE NOT NULL,
    CLOVER_EMAIL TEXT UNIQUE NOT NULL,
    CLOVER_PWD TEXT NOT NULL,
    nKEY TEXT NOT NULL)"""
cur.execute(tbl1_ddl)

mac = hex(get_mac())

tbl1_ddl = """CREATE TABLE if not exists CLOVER_VARIABLES (
    SERIAL_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    VARIABLES INTEGER NOT NULL,
    nKEY TEXT NOT NULL)"""
cur.execute(tbl1_ddl)

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

# db.close()


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
