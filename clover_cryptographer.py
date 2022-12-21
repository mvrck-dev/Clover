import Crypto.Cipher.AES as AES
from base64 import *
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


