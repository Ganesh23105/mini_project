from tkinter import *
import pymysql
from tkinter import messagebox
from tkcalendar import DateEntry
from tkinter import ttk

student_register_window=Tk()
student_register_window.title("STUDENT REGISTER")
student_register_window.geometry("500x500")

student_fname_label=Label(student_register_window,text="FNAME")
student_fname_label.grid(row=0,column=0,padx=50)
student_fname_entry=Entry(student_register_window)
student_fname_entry.grid(row=1,column=0)

student_mname_label=Label(student_register_window,text="MNAME")
student_mname_label.grid(row=0,column=4,padx=50)
student_mname_entry=Entry(student_register_window)
student_mname_entry.grid(row=1,column=4)  

student_lname_label=Label(student_register_window,text="LNAME")
student_lname_label.grid(row=0,column=8,padx=50)
student_lname_entry=Entry(student_register_window)
student_lname_entry.grid(row=1,column=8)

student_DOB_label=Label(student_register_window,text="DOB",pady=10)
student_DOB_label.grid(row=2,column=0)
student_birth_date = DateEntry(student_register_window)
student_birth_date.grid(row=3,column=0)

student_age_label=Label(student_register_window,text="Age")
student_age_label.grid(row=2,column=4)
student_age_entry=Entry(student_register_window)
student_age_entry.grid(row=3,column=4)

student_phone_number_label=Label(student_register_window,text="Phone Number")
student_phone_number_label.grid(row=4,column=0)
student_phone_number_entry=Entry(student_register_window)
student_phone_number_entry.grid(row=4,column=4,pady=10)

student_college_id_label=Label(student_register_window,text="College ID")
student_college_id_label.grid(row=5,column=0)
student_college_id_entry=Entry(student_register_window)
student_college_id_entry.grid(row=5,column=4,pady=10)

student_college_name_label=Label(student_register_window,text="COLLEGE NAME")
student_college_name_label.grid(row=6,column=0)
student_college_name_entry=Entry(student_register_window)
student_college_name_entry.grid(row=6,column=4,pady=10)

student_college_stream_label=Label(student_register_window,text="STREAM")
student_college_stream_label.grid(row=7,column=0,pady=10)
combo_var_stream=StringVar()
combo_box_stream =ttk.Combobox(student_register_window, textvariable=combo_var_stream)
combo_box_stream['values'] = ('Option 1', 'Option 2', 'Option 3', 'Option 4')
combo_box_stream.grid(row=7,column=4)
combo_box_stream.set("")

student_college_year_label=Label(student_register_window,text="Year")
student_college_year_label.grid(row=9,column=0,pady=10)
combo_var_year=StringVar()
combo_box_year=ttk.Combobox(student_register_window,textvariable=combo_var_year)
combo_box_year['values'] = ('1st year', 'Option 2', 'Option 3', 'Option 4')
combo_box_year.grid(row=9, column=4)
combo_box_year.set("")

student_college_division_label=Label(student_register_window,text="division")
student_college_division_label.grid(row=10,column=0,pady=10)
student_college_division_entry=Entry(student_register_window)
student_college_division_entry.grid(row=10,column=4)

student_college_roll_no_label=Label(student_register_window,text="roll no")
student_college_roll_no_label.grid(row=11,column=0,pady=10)
student_college_roll_no_entry=Entry(student_register_window)
student_college_roll_no_entry.grid(row=11,column=4)

student_submit_button=Button(student_register_window,text="SUBMIT")
student_submit_button.grid(row=14,column=4)






student_register_window.mainloop()