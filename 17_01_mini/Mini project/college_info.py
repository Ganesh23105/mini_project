from tkinter import *
from tkinter import messagebox
import pymysql

def add():
    if stream_entry.get()==""and year_entry.get()=="":
        messagebox.showerror("error","stream and no of years are required",parent=college_info_window)
    else:
        try:
            con = pymysql.connect(host='localhost',user='root',password='root')
            mycursor = con.cursor()
        except:
            messagebox.showerror('Error','Connection is not established try again.')
            return    
        query = 'use concession'
        mycursor.execute(query)

        try:
            query='create table stream(college_id int,S_name varchar(100),course varchar(100),)'

        


college_info_window=Toplevel()
college_info_window.title("COLLEGE INFO")
college_info_window.geometry("500x500")

stream_label=Label(college_info_window,text="stream name")
stream_label.grid(row=0,column=0)
stream_entry=Entry(college_info_window)
stream_entry.grid(row=0,column=1)



course_label=Label(college_info_window,text="course name")
course_label.grid(row=1,column=0)
course_entry=Entry(college_info_window)
course_entry.grid(row=1,column=1)

year_label=Label(college_info_window,text="no of years")
year_label.grid(row=2,column=0)
year_entry=Entry(college_info_window)
year_entry.grid(row=2,column=1)

add_button=Button(college_info_window,text="ADD",command=add)
add_button.grid(row=3,column=0,columnspan=2)



#college_id_entry.bind('<Return>',lambda event:college_name_entry.focus())

stream_entry.bind('<Return>',lambda event:course_entry.focus())
course_entry.bind('<Return>',lambda event:year_entry.focus())
 
college_info_window.mainloop()
