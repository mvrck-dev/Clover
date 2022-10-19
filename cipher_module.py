import Crypto.Cipher.AES as AES
from hashlib import sha256
from secrets import shift_key

#CIPHER ENCRYPTION
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def caesar_encrypt(plain_text, shift_key):
  cipher_text = ""
  for letter in plain_text:
    position = alphabet.index(letter)
    new_position = position + shift_key
    cipher_text += alphabet[new_position]
  print(f"The encoded text is {cipher_text}")


def caesar_decrypt(cipher_text, shift_key):
  plain_text = ""
  for letter in cipher_text:
    position = alphabet.index(letter)
    new_position = position - shift_key
    plain_text += alphabet[new_position]
  print(f"The decoded text is {plain_text}")


# AES ENCRYPTION
key = b"Hello"
hkey = sha256(key.encode()).digest()

def aes_encrypt(hkey, appname, app_password):
    presalt = caesar_encrypt(appname, 5)
    saltpwd = presalt + app_password
    cipher = AES.new(hkey, AES.MODE_ECB)
    return cipher.encrypt(saltpwd)

def aes_decrypt(hkey, appname, app_password):
    cipher = AES.new(hkey, AES.MODE_ECB)
    saltdecrtypt = cipher.decrypt(app_password)
    presalt = caesar_decrypt(appname, 5)
    orig_pwd = saltdecrtypt.replace(presalt, "")
    return orig_pwd
    
    


