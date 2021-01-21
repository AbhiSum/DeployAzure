import tkinter as tk 
from tkinter import ttk
from tkinter import *
import pandas as pd
import tkinter.messagebox 
import sqlite3 as sl
import re
from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return trial()



def trial():
    
    try:
        
        # Setting up connection to the db
        conn = sl.connect("D:\\OJT\\IP_Deployment OJT\\data.sqllite")	
        
        #Creating Cursor object method to perform SQL queries 
        cur = conn.cursor()
        
        #checking if I have got desired output or not 
        cur.execute("SELECT * FROM employees").fetchall() 
    
        def form():
            root1 = Tk()
            root1.geometry("400x350")
            root1.title('Login Form')
            
            def clean_name(some_var):
                return ''.join(char for char in some_var if char.isalnum())
            
            def check():
                if(entry_1.get()!="" and entry_2.get()!=""):
                    cur.execute('SELECT * FROM employees WHERE Username = "' + entry_1.get() + '" AND Password = "' + entry_2.get() + '"') # AND Password = "' + entry_2.get() + '"
                    #cur.execute("SELECT Username, Password FROM employees WHERE Username = '%(user)s'" % { 'user' : entry_1.get()} )
                    result = cur.fetchall()
                    if result != None:
                        #uname, passw = result
                        print("valid")
                        print(result)
                    else:
                        print("Invalid")
                else:  
                    tkinter.messagebox.showinfo("Invalid","Missing Entry", parent=root1)
                
    
    
            def close():
                root1.destroy()
                
            #user_details
            label_0 =Label(root1,text="User Details",bg='Brown',fg='white',width=20,font=("bold",15))
            label_0.place(x=80,y=30)
            
            #username
            label_1 =Label(root1,text="Username:", width=20,font=("bold",12))
            label_1.place(x=10,y=100)
            
            global entry_1
            entry_1=Entry(root1,width=30)
            entry_1.place(x=180,y=100)
            
            
            #password
            label_2 =Label(root1,text="Password:", width=20,font=("bold",12))
            label_2.place(x=10,y=170)
            
            global entry_2
            entry_2=Entry(root1,width=30) #, show="*"
            entry_2.place(x=180,y=170)
            
            
            Button(root1, text='Login' , width=20,bg="Green",fg='white', command = check).place(x=30,y=250)
            Button(root1, text='Exit' , width=20,bg="Grey",fg='white', command = close).place(x=200,y=250)
            
            root1.mainloop()
            
            
        
        form()
    
    
    except FileNotFoundError:
        print("This file doesn't exist")
        
    except sl.OperationalError:
        print("This table doesn't exist")
        
    except sl.DatabaseError:
        print("This column doesn't exist")
        
    except Exception as e:
        print("Error: " ,e)
      
    finally:
        #Closing the connection 
         conn.close()
    


