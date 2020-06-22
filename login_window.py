import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import tkcalendar as tkc
from user import User

class LoginWindowApp(tk.Frame):



    def __init__(self, user, master=None):
        super().__init__(master)
        self._user = user
        self._name_entry = None
        self._login_entry = None
        self._password_entry = None
        self.logged = False
        self.pack()
        self.execute_login_window()

    def execute_login_window(self):
        self.generate_name_section()
        self.generate_login_section()
        self.generate_password_section()
        self.generate_submit_btn()

    def generate_name_section(self):
        frame = tk.Frame(self)
        frame.pack()

        name_label = tk.Label(frame, text="Enter your name")
        name_label.pack(side=tk.LEFT)

        self._name_entry = tk.Entry(frame)
        self._name_entry.pack(side=tk.LEFT)

    def generate_login_section(self):
        frame = tk.Frame(self)
        frame.pack()

        login_label = tk.Label(frame, text="Enter your login")
        login_label.pack(side=tk.LEFT)

        self._login_entry = tk.Entry(frame)
        self._login_entry.pack(side=tk.LEFT)

    def generate_password_section(self):
        frame = tk.Frame(self)
        frame.pack()

        password_label = tk.Label(frame, text="Enter your password")
        password_label.pack(side=tk.LEFT)

        self._password_entry = tk.Entry(frame)
        self._password_entry.pack(side=tk.LEFT)

    def generate_submit_btn(self):
        frame=tk.Frame(self)
        frame.pack()

        submit_btn = tk.Button(self, text='Login', command=self.log_in)
        submit_btn.pack(side=tk.BOTTOM)

    def log_in(self):
        name = self._name_entry.get()
        login = self._login_entry.get()
        password = self._password_entry.get()
        user = self._user
        if user.is_authorized(name, login, password):
            self.logged = True
            user.users.append(user)
            self.master.destroy()
        else:
            messagebox.askyesno(title="Login error", message="Credentials failed, do you want to retry?")

