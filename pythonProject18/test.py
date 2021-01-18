from tkinter import *
import mysql.connector
import tkinter as tk
from tkinter import messagebox

mydb= mysql.connector.connect(user='lifechoices', password='@Lifechoices1234',host='127.0.0.1',database='hospital',auth_plugin='mysql_native_password')
mycursor=mydb.cursor()

def verify():
    user_verify = username.get()
    pass_verify= password.get()
    sql= "select * from Login where username = %s and password = %s"
    mycursor.execute(sql, [(user_verify), (pass_verify)])
    results = mycursor.fetchall()
    if results:
        for i in results:
            messagebox.showinfo("You have successfully logged")
            # logged()
            # break

        else:
            messagebox.showinfo("wrong login")

# def logged():
#     messagebox.showinfo("You have successfully logged")



# def failed():
#     messagebox.showinfo("wrong login")

def sign():
    if regbtn:
        window.withdraw()
        import reg
        reg.reg()

window= tk.Tk()
window.title("Login page")
window.geometry("450x450")

lbuse = tk.Label(window, text="Enter username")
lbuse.place(x=50, y=20)

username = tk.Entry(window, width=35)
username.place(x=250, y=20, width=100)

lbpass = tk.Label(window, text="Enter password")
lbpass.place(x=50, y=50)

password = tk.Entry(window, width=35)
password.place(x=250, y=50, width=100)

lnum = tk.Label(window, text="Enter Phone-Number")
lnum.place(x=50, y=80)

numb = tk.Entry(window, width=35)
numb.place(x=250, y=80, width=100)

logbtn= tk.Button(window, text="Login", bg="blue", command=verify)
logbtn.place(x=50, y=135, width=55)

regbtn=tk.Button(window, text="Register", bg="blue", command=sign)
regbtn.place(x=150, y=135, width=150)

window.mainloop()