import pandas as pd
import sqlite3 as sl
from cryptography.fernet import Fernet

# Generating the key and writing it to a file
def genwrite_key():
    key = Fernet.generate_key()
    with open("D:\\OJT\\IP_Deployment OJT\\pass.key", "wb") as key_file:
        key_file.write(key)
genwrite_key()

def call_key():
    return open("D:\\OJT\\IP_Deployment OJT\\pass.key", "rb").read()

           
key = call_key()
a = Fernet(key)

# Setting up connection to the db
conn = sl.connect("D:\\OJT\\IP_Deployment OJT\\data.sqllite")	

#Creating Cursor object method to perform SQL queries 
cur = conn.cursor()

# loading the data into a Pandas DataFrame
file = pd.read_csv("D:\\OJT\\IP_Deployment OJT\\data.csv")

def encrp(s):
    j=0
    for i in list(file[s]):
        #print(i)
        i = str(i)
        conv = a.encrypt(str.encode(i)).decode()
        #print(file.loc[j,'Password'])
        file.loc[j,s] = conv
        j = j + 1

encrp("Password")
encrp("Address")
encrp("Phone")
"""
for i in list(file["Address"]):
    print(a.decrypt(i.encode()).decode())
"""
file.to_csv("D:\\OJT\\IP_Deployment OJT\\edata.csv", index = False)

# Writing data into SQLLite table
file.to_sql("employees", conn, if_exists='replace',index=False)

#checking if I have got desired output or not 
cur.execute("SELECT * FROM employees").fetchall()

file2 = pd.read_csv("D:\\OJT\\IP_Deployment OJT\\carddata.csv")
def encrp2(s):
    j=0
    for i in list(file2[s]):
        #print(i)
        i = str(i)
        conv = a.encrypt(str.encode(i)).decode()
        #print(file.loc[j,'Password'])
        file2.loc[j,s] = conv
        j = j + 1

encrp2("Card")
encrp2("Pin")
encrp2("CVV")
"""
for i in list(file["Card"]):
    print(a.decrypt(i.encode()).decode())
"""
file2.to_csv("D:\\OJT\\IP_Deployment OJT\\ecarddata.csv", index = False)

file2.to_sql("card", conn, if_exists='replace',index=False)

cur.execute("SELECT * FROM card").fetchall()

