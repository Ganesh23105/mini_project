from tkinter import *

student_login_window=Tk()

student_login_window.title("student_login_window")
student_login_window.geometry("500x500")

student_username_label=Label(student_login_window,text="USERNAME")
student_username_label.grid(row=0,column=0)

student_username_entry=Entry(student_login_window)
student_username_entry.grid(row=0,column=1)


student_password_label=Label(student_login_window,text="PASSWORD")
student_password_label.grid(row=1,column=0)

student_password_entry=Entry(student_login_window)
student_password_entry.grid(row=1,column=1)

student_login_button=Button(student_login_window,text="LOGIN")
student_login_button.grid(row=2,column=0,columnspan=2)

not_register_label=Label(student_login_window,text="NOT YET REGISTER")
not_register_label.grid(row=4,column=0)

register_btton=Button(student_login_window,text="REGISTER?")
register_btton.grid(row=4,column=1)


student_login_window.mainloop()