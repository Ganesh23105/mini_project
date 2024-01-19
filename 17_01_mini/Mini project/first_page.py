from tkinter import *

def admin_page():
    first_window.destroy()
    import admin_login
     
def student_page():
    first_window.destroy()
    import student_login

first_window=Tk()

first_window.title("HOME")
first_window.geometry("500x500")

adminbutton=Button(first_window,text="ADMIN",command=admin_page)
adminbutton.grid(row=0,column=0)

studentbutton=Button(first_window,text="STUDENT",command=student_page)
studentbutton.grid(row=0,column=1)

first_window.mainloop()