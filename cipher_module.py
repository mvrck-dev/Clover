import Crypto.Cipher.AES as AES
from base64 import b64encode
from Crypto.Util.Padding import pad, unpad
from hashlib import sha256
import secrets
import hashlib
import random
import sqlite3 as sql
from uuid import getnode as get_mac
mac = hex(get_mac())

activedb = sql.connect("CLOVER_DB.db")
cur = activedb.cursor()


tbl1_ddl = """CREATE TABLE if not exists CLOVER_VARIABLES (
    SERIAL_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    VARIABLES INTEGER NOT NULL,
    nKEY TEXT NOT NULL)"""
cur.execute(tbl1_ddl)


#CIPHER ENCRYPTION : To generate a unique Salt for encryption
characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '!', '_']
def caesar_encrypt(plain_text, shift_key):
  cipher_text = ""
  for letter in plain_text:
    position = characters.index(letter)
    new_position = position + shift_key
    cipher_text += characters[new_position]
  # print(f"The encoded text is {cipher_text}") #Testing``
  return cipher_text


def caesar_decrypt(cipher_text, shift_key):
  plain_text = ""
  for letter in cipher_text:
    position = characters.index(letter)
    new_position = position - shift_key
    plain_text += characters[new_position]
  # print(f"The decoded text is {plain_text}")  #Testing
  return plain_text

#HASHING STATION
def hash(pwd, salt):
    hash = salt + pwd
    hashed_string = hashlib.sha256(hash.encode('utf-8')).hexdigest()
    return hashed_string

#PASSWORD GENRATOR
def pwd_generator():
  letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
             'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
  symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
  nr_letters = 10
  nr_symbols = 4
  nr_numbers = 6
  password_list = []
  for char in range(1, nr_letters + 1):
      password_list += random.choice(letters)
  for char in range(1, nr_symbols + 1):
      password_list += random.choice(symbols)
  for char in range(1, nr_numbers + 1):
      password_list += random.choice(numbers)
  random.shuffle(password_list)
  password = ''
  for char in password_list:
      password += char
  return password
  
# AES ENCRYPTION
# def hkey(key):
#     return hashlib.sha256(key.encode()).digest()
# # key = f"{secrets.aes_key}"
# hkey = sha256(key.encode()).digest()

# def aes_encrypt(hkey, appname, app_password):
#     presalt = caesar_encrypt(appname, 5)
#     saltpwd = presalt + app_password

#     cipher = AES.new(hkey, AES.MODE_ECB, )
#     return cipher.encrypt(saltpwd)

def aes_encrypt(key, appname, app_password):
    hkey = bytes(hashlib.sha256(str(key).encode()).digest(), 'utf-8')
    iv = bytes(caesar_encrypt(appname, 5), 'utf-8')
    cipher = AES.new(hkey, AES.MODE_CBC, iv)
    encrypted = cipher.encrypt(pad(app_password.encode("UTF-8"), AES.block_size))
    return b64encode(encrypted).decode('utf-8')      
    

# def aes_decrypt(hkey, appname, app_password):
#     cipher = AES.new(hkey, AES.MODE_ECB)
#     saltdecrtypt = cipher.decrypt(app_password)
#     presalt = caesar_decrypt(appname, 5)
#     orig_pwd = saltdecrtypt.replace(presalt, "")
#     return orig_pwd
    
def aes_decrypt(key, appname, app_password):
    hkey = bytes(hashlib.sha256(str(key).encode()).digest(), 'utf-8')
    iv = bytes(caesar_encrypt(appname, 5), 'utf-8')
    cipher = AES.new(hkey, AES.MODE_CBC, iv)
    decrypted = cipher.decrypt(pad(app_password.encode("UTF-8"), AES.block_size))
    return b64encode(decrypted).decode('utf-8')      
    


