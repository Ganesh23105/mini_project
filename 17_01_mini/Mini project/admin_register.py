from tkinter import *
import pymysql
from tkinter import messagebox

def login_page():
    admin_window.destroy()
    import admin_login

def register():
    if college_id_entry.get()==''and college_name_entry.get()==''and college_place_entry.get()==''and college_address_entry.get()==''and college_email_entry.get()==''and college_admin_name_entry.get()==''and college_Admin_email_entry.get()==''and college_password_entry.get()==''and college_confirm_password_entry.get()=='':
        messagebox.showerror('Error','All fields are required.')
    else:
        try:
            con = pymysql.connect(host='localhost',user='root',password='Ganesh@23105')
            mycursor = con.cursor()
        except:
            messagebox.showerror('Error','Database Connectivity Issue, Please Try Again.')
            return
        try:
            query='create database concession'
            mycursor.execute(query)
            query='use concession'
            mycursor.execute(query)
            query = 'create table admin(college_id int primary key not null, college_name varchar(100), college_place varchar(25), college_address varchar(255), college_email varchar(40), college_admin varchar(40), admin_email varchar(40), college_password varchar(20))'
            mycursor.execute(query)
        except:
            query='use concession'
            mycursor.execute(query)

        query = 'select * from admin where college_id=%s'
        mycursor.execute(query,(college_id_entry.get()))
        row = mycursor.fetchone()

        if row != None:
            messagebox.showerror('Error','College_ID Already Exists')
        elif college_password_entry.get()!=college_confirm_password_entry.get():
            messagebox.showerror('Error','Password does not match.') 
        else:
            query = 'insert into admin(college_id, college_name, college_place, college_address, college_email, college_admin,admin_email,college_password) values(%s,%s,%s,%s,%s,%s,%s,%s)'
            mycursor.execute(query,(college_id_entry.get(),college_name_entry.get(),college_place_entry.get(),college_address_entry.get(),college_email_entry.get(),college_admin_name_entry.get(),college_Admin_email_entry.get(),college_password_entry.get()))
            con.commit()
            con.close()
            messagebox.showinfo('Success','Registration is Successful')

            clear()
            
            admin_window.destroy()
            import admin_home


def clear():
    college_id_entry.delete(0,END)
    college_name_entry.delete(0,END)
    college_place_entry.delete(0,END)
    college_address_entry.delete(0,END)
    college_email_entry.delete(0,END)
    college_admin_name_entry.delete(0,END)
    college_Admin_email_entry.delete(0,END)
    college_password_entry.delete(0,END)
    college_confirm_password_entry.delete(0,END)



admin_window=Tk()

admin_window.title("ADMIN")
admin_window.geometry("500x500")

college_id_label=Label(admin_window,text="College ID")
college_id_label.grid(row=0,column=0)
college_id_entry=Entry(admin_window)
college_id_entry.grid(row=0,column=1)

college_name_label=Label(admin_window,text="College Name")
college_name_label.grid(row=1,column=0)
college_name_entry=Entry(admin_window)
college_name_entry.grid(row=1,column=1)

college_place_label=Label(admin_window,text="Nearest Station/Stop")
college_place_label.grid(row=2,column=0)
college_place_entry=Entry(admin_window)
college_place_entry.grid(row=2,column=1)

college_address_label=Label(admin_window,text="College address")
college_address_label.grid(row=3,column=0)
college_address_entry=Entry(admin_window)
college_address_entry.grid(row=3,column=1)

college_email_label=Label(admin_window,text="College Email")
college_email_label.grid(row=4,column=0)
college_email_entry=Entry(admin_window)
college_email_entry.grid(row=4,column=1)

college_admin_name_label=Label(admin_window,text="Admin Name")
college_admin_name_label.grid(row=5,column=0)
college_admin_name_entry=Entry(admin_window)
college_admin_name_entry.grid(row=5,column=1)

college_Admin_email_label=Label(admin_window,text="Admin Email")
college_Admin_email_label.grid(row=6,column=0)
college_Admin_email_entry=Entry(admin_window)
college_Admin_email_entry.grid(row=6,column=1)

college_password_label=Label(admin_window,text="Password")
college_password_label.grid(row=7,column=0)
college_password_entry=Entry(admin_window)
college_password_entry.grid(row=7,column=1)

college_confirm_password_label=Label(admin_window,text="Confirm Password")
college_confirm_password_label.grid(row=8,column=0)
college_confirm_password_entry=Entry(admin_window)
college_confirm_password_entry.grid(row=8,column=1)

Register_button=Button(admin_window,text="Register",command=register)
Register_button.grid(row=9,column=0,columnspan=2)

login_label=Label(admin_window,text="Already Register")
login_label.grid(row=10,column=0,pady=10)

loginbutton=Button(admin_window,text="Login",command= login_page)

loginbutton.grid(row=10,column=1)

college_id_entry.bind('<Return>',lambda event:college_name_entry.focus())
college_name_entry.bind('<Return>',lambda event:college_place_entry.focus())
college_place_entry.bind('<Return>',lambda event:college_address_entry.focus())
college_address_entry.bind('<Return>',lambda event:college_email_entry.focus())
college_email_entry.bind('<Return>',lambda event:college_admin_name_entry.focus())
college_admin_name_entry.bind('<Return>',lambda event:college_Admin_email_entry.focus())
college_Admin_email_entry.bind('<Return>',lambda event:college_password_entry.focus())
college_password_entry.bind('<Return>',lambda event:college_confirm_password_entry.focus())


  
admin_window.mainloop()