import sqlite3 as sql
import subprocess
import sys
from uuid import getnode as get_mac
import hashlib

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
        if package_init() >= 100:
            print(package_init())
            print("All packages are installed")
        else:
            print(package_init())
            print("Some packages are not installed")
            print("Please install the missing packages")
            print("Then restart the program")
    return n

package_init()

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
    cur.execute(f"INSERT INTO CLOVER_MASTERDB(VARIABLE, nKEY) VALUES('MASTER', '{hashed_mac}')")
    activedb.commit()
    activedb.close()

db_init()