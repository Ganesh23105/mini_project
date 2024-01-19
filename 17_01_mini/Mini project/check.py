import tkinter as tk
from tkinter import messagebox
import pymysql

class AdminApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ADMIN")
        self.root.geometry("500x500")

        # Variables for entry fields
        self.college_id_var = tk.StringVar()
        self.college_name_var = tk.StringVar()
        self.college_place_var = tk.StringVar()
        self.college_address_var = tk.StringVar()
        self.college_email_var = tk.StringVar()
        self.college_admin_name_var = tk.StringVar()
        self.college_Admin_email_var = tk.StringVar()
        self.college_password_var = tk.StringVar()
        self.college_confirm_password_var = tk.StringVar()

        # Set up frames
        self.frame_login = tk.Frame(root)
        self.frame_register = tk.Frame(root)

        # Initialize the GUI
        self.init_login_frame()
        self.init_register_frame()

    def init_login_frame(self):
        self.frame_login.grid(row=0, column=0, sticky="nsew")

        college_id_label = tk.Label(self.frame_login, text="COLLEGE ID")
        college_id_label.grid(row=0, column=0)

        college_id_entry = tk.Entry(self.frame_login, textvariable=self.college_id_var)
        college_id_entry.grid(row=0, column=1)

        submit_button = tk.Button(self.frame_login, text="VERIFY", command=self.verify)
        submit_button.grid(row=0, column=2)

        # ... Other widgets for login frame ...

    def init_register_frame(self):
        self.frame_register.grid(row=0, column=0, sticky="nsew")

        college_id_label = tk.Label(self.frame_register, text="College ID")
        college_id_label.grid(row=0, column=0)
        college_id_entry = tk.Entry(self.frame_register, textvariable=self.college_id_var)
        college_id_entry.grid(row=0, column=1)

        # ... Other widgets for register frame ...

    def verify(self):
        # Implement your verification logic here
        pass

    def register(self):
        # Implement your registration logic here
        pass

if __name__ == "__main__":
    root = tk.Tk()
    app = AdminApp(root)
    root.mainloop()
