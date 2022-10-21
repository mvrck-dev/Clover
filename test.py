import cipher_module

# text_in = input("Enter username to encrypt: ")
# shift = 23

# cipher_text = cipher_module.caesar_encrypt(text_in, shift)
# print(f"The encoded text is {cipher_text}")

# usr_pwd = input("Enter password: ")

# key = cipher_module.hash(usr_pwd, cipher_text) #Key
# print(key)
# #HKey

# appname = input("Enter app name: ")
# app_password = input("Enter app password: ")
 
# cipher_pwd = cipher_module.aes_encrypt(key, appname, app_password)
# print(f"Cipher Pwd{cipher_pwd}")

# decrypted_pwd = cipher_module.aes_decrypt(key, appname, cipher_pwd)
# print(f"Deciphered Pwd{decrypted_pwd}")

print(cipher_module.pwd_generator())