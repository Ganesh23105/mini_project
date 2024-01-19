from tkinter import *

def college_info():
    import college_info




admin_home_window=Tk()
admin_home_window.geometry("500x500")
admin_home_window.title("ADMIN HOME")

college_info_button=Button(admin_home_window,text="college info",command=college_info)
college_info_button.grid(row=0,column=0)

student_verify=Button(admin_home_window,text="verify student")
student_verify.grid(row=1,column=0)





admin_home_window.mainloop()