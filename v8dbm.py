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

