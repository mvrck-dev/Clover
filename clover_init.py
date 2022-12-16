import subprocess
import sqlite3 as sql
import sys
from uuid import getnode as get_mac
import hashlib
import time

if sys.version >= '3.9':
    print('Your Python version is above 3.9')
    print('Checking Packages')
    time.sleep(2)
else:
    print('Your Python version is not above 3.9')
    print('Please update your Python version')
    time.sleep(2)
    exit()

div = 100/10
n = 0

try:
    import re
    print("re is installed")
    n = div
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
print("If the code breaks down in the next step please run the program again.")
time.sleep(2)
try:
    import PyQt6
    print("PyQt6 is installed")
    n += div
except ImportError:
    print("PyQt6 is not installed")
    print("installing PyQt6")
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'PyQt6'])
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'pyqt6-tools'])
    print("PyQt6 is now installed")
    import PyQt6
    n += div
if n == 100:
    print("All Packages are installed\nInitialising Clover[main.py]")
else:
    print("Some Packages are not installed")
    print("Please try again")
    time.sleep(2)
    exit()

def db_init():
    activedb = sql.connect("CLOVER_DB.db")
    cur = activedb.cursor()

    tbl1_ddl = """CREATE TABLE if not exists CLOVER_MASTERDB (
        SERIAL_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        CLOVER_USRNM TEXT UNIQUE NOT NULL,
        CLOVER_EMAIL TEXT UNIQUE NOT NULL,
        CLOVER_PWD TEXT NOT NULL,
        nKEY TEXT NOT NULL)"""
    cur.execute(tbl1_ddl)

    tbl2_ddl = """CREATE TABLE if not exists CLOVER_VARIABLES (
        SERIAL_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        VARIABLE TEXT NOT NULL,
        nKEY TEXT NOT NULL)"""
    cur.execute(tbl2_ddl)

    mac = hex(get_mac())
    hashed_mac = hashlib.sha256(mac.encode('utf-8')).hexdigest()
    cur.execute(f"INSERT INTO CLOVER_VARIABLES(VARIABLE, nKEY) VALUES('MASTER', '{hashed_mac}')")
    activedb.commit()
    activedb.close()

db_init()