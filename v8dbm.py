import mysql.connector as dbcn


# Initialising Database
activedb = dbcn.connect(host = "localhost", user = "root", password= "destiny012", database = "Vault8")
print("Initialised MySql Database Connection.")
cur = activedb.cursor()

# Setting Up Databases
cur.execute(f"CREATE DATABASE if not exists Vault8")
print("Database has been successfully created.")
cur.execute("USE Vault8")
print("Database Vault8 is Active.")
cur.execute(f"CREATE TABLE if not exists master_login_db(userid int(5) PRIMARY KEY, username varchar(20) NOT NULL UNIQUE, email varchar(50) NOT NULL UNIQUE, password varchar(1000) NOT NULL);")
print("Master Login is now active")
# cur.execute(f"CREATE TABLE if not exists master_login_db(userid int(5), username varchar(20) NOT NULL, appname(20) NOT NULL, app_password varchar(1000) NOT NULL);")
# print("Master Login is now active")

#insert into master_login_db values(0001, 'ray', 'concepts.ray@gmail.com', '08ed649a54beeca6e677962ea65ce7ea20267dc0ce4a0c88b6a6d5bdf22a5e71');
