from tkinter import *
import pymysql
from tkinter import messagebox

def login():

    try:
        con = pymysql.connect(host='localhost',user='root',password='Ganesh@23105')
        mycursor = con.cursor()
    except:
        messagebox.showerror('Error','Connection is not established try again.')
        return

    query = 'use concession'
    mycursor.execute(query)
    query='SELECT college_password FROM admin WHERE college_id=%s'
    mycursor.execute(query,college_id_entry.get())
    # for newpassword
    sql_password=mycursor.fetchone()
    # print(sql_password)
    # print(type(sql_password))
    if password_entry.get()!=sql_password[0]:
        messagebox.showerror('ERROR','INVALID PASSWORD')
    else:
        messagebox.showinfo('Success','LOGIN SUCCESSFUL')
        admin_window.destroy()
        import admin_home




def verify():
    if college_id_entry.get()==''and password_entry.get()=='':
        messagebox.showerror('Error','COLLEGE ID REQUIRED')
    else:
        try:
            con = pymysql.connect(host='localhost',user='root',password='Ganesh@23105')
            mycursor = con.cursor()
        except:
            messagebox.showerror('Error','Connection is not established try again.')
            return

        query = 'use concession'
        mycursor.execute(query)
        query = 'select * from admin where college_id=%s'
        mycursor.execute(query,(college_id_entry.get()))

        row=mycursor.fetchone()
        if row == None:
            messagebox.showerror('Error','INVALID COLLEGE ID')
        else:
            query='SELECT college_name,college_place FROM admin WHERE college_id=%s'
            mycursor.execute(query,college_id_entry.get())
            tup=mycursor.fetchone()
            #print(tup[0])
            college_name_entry.config(state=NORMAL)
            college_place_entry.config(state=NORMAL)
            college_name_entry.delete(0,END)
            college_place_entry.delete(0,END)
            college_name_entry.insert(0,tup[0])
            college_place_entry.insert(0,tup[1])
            college_name_entry.config(state=DISABLED)
            college_place_entry.config(state=DISABLED)


            password_entry.focus_set()
            

        


def register_page():
    admin_window.destroy()
    import admin_register

admin_window=Tk()

admin_window.title("ADMIN")
admin_window.geometry("500x500")

college_id_label=Label(admin_window,text="COLLEGE ID")
college_id_label.grid(row=0,column=0)

college_id_entry=Entry(admin_window)
college_id_entry.grid(row=0,column=1)

submit_button=Button(admin_window,text="VERIFY",command=verify)
submit_button.grid(row=0,column=2)

college_name_label=Label(admin_window,text="COLLEGE NAME")
college_name_label.grid(row=1,column=0)

college_name_entry=Entry(admin_window)
college_name_entry.grid(row=1,column=1)
college_name_entry.config(state=DISABLED)

college_place_label=Label(admin_window,text="COLLEGE PLACE")
college_place_label.grid(row=2,column=0)

college_place_entry=Entry(admin_window)
college_place_entry.grid(row=2,column=1)
college_place_entry.config(state=DISABLED)

password_label=Label(admin_window,text="PASSWORD")
password_label.grid(row=3,column=0)

password_entry=Entry(admin_window)
password_entry.grid(row=3,column=1)

loginbutton=Button(admin_window,text="LOGIN",command=login)
loginbutton.grid(row=4,column=0,columnspan=2)

register_label=Label(admin_window,text="NOT YET REGISTER ?")
register_label.grid(row=5,column=1,pady=10)

registerbutton=Button(admin_window,text="REGISTER",command=register_page)
registerbutton.grid(row=5,column=2)

admin_window.mainloop()