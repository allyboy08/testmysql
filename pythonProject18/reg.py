from tkinter import *
import mysql.connector
import tkinter as tk
from tkinter import messagebox

def verify():
    # user_verify = username.get()
    # pass_verify= password.get()
    # sql= "select * from Login where username = %s and password = %s"
    # mycursor.execute(sql, [(user_verify), (pass_verify)])
    # results = mycursor.fetchall()
    if logbtn:
        window.withdraw()
        import test
        test.test()

window= tk.Tk()
window.title("Login page")
window.geometry("450x450")

fname = tk.Label(window, text="Name")
fname.place(x=50, y=20)

name = tk.Entry(window, width=35)
name.place(x=250, y=20, width=100)

lname = tk.Label(window, text="Last Name")
lname.place(x=50, y=50)

surname = tk.Entry(window, width=35)
surname.place(x=250, y=50, width=100)

user = tk.Label(window, text="Username")
user.place(x=50, y=80)

use = tk.Entry(window, width=35)
use.place(x=250, y=80, width=100)

lpass = tk.Label(window, text="Password ")
lpass.place(x=50, y=80)

passw = tk.Entry(window, width=35)
passw.place(x=250, y=80, width=100)

logbtn= tk.Button(window, text="Login", bg="blue", command=verify)
logbtn.place(x=150, y=135, width=55)

window.mainloop()