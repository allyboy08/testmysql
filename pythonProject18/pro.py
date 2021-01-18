from tkinter import *
import mysql.connector
import tkinter as tk

# mydb= mysql.connector.connect(user='lifechoices', password='@Lifechoices1234',host='127.0.0.1',database='hospital',auth_plugin='mysql_native_password')
# mycursor=mydb.cursor()


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



def sign():
    if regbtn:
        window.withdraw()
        import reg
        reg.reg()


window= tk.Tk()
window.title("Login page")
window.geometry("450x450")



logbtn= tk.Button(window, text="Login", bg="blue", command=verify)
logbtn.place(x=150, y=135, width=55)

regbtn=tk.Button(window, text="Register", bg="blue", command=sign)
regbtn.place(x=250, y=135, width=150)

window.mainloop()