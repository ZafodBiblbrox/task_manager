import tkinter as tk
from tkinter import messagebox
from user import User
import initial_window
from database import SimpleDataBase


class Account(tk.Frame):

    def __init__(self, master_frame, controller, db):
        super().__init__(master_frame)
        self._user = User()
        #self._db = SimpleDataBase('task_manager.db', 'task_manager_schema.txt')
        self._db = db
        self._name_entry = None
        self._login_entry = None
        self._password_entry = None
        self.controller = controller
        self.execute_window()

    def execute_window(self):
        self.generate_name_section()
        self.generate_login_section()
        self.generate_password_section()
        self.generate_submit_btn()
        self.generate_goto_btn(initial_window.InitialWindow, text='Back to initial')


    def generate_name_section(self):
        frame = tk.Frame(self)
        frame.pack()

        name_label = tk.Label(self, text="Enter your name")
        name_label.pack()

        self._name_entry = tk.Entry(self)
        self._name_entry.pack()

    def generate_login_section(self):
        frame = tk.Frame(self)
        frame.pack()

        login_label = tk.Label(self, text="Enter your login")
        login_label.pack()

        self._login_entry = tk.Entry(self)
        self._login_entry.pack()

    def generate_password_section(self):
        frame = tk.Frame(self)
        frame.pack()

        password_label = tk.Label(self, text="Enter your password")
        password_label.pack()

        self._password_entry = tk.Entry(self)
        self._password_entry.pack()

    def generate_submit_btn(self):
        frame = tk.Frame(self)
        frame.pack()

        submit_btn = tk.Button(self, text='Create account', command=self.create_account)
        submit_btn.pack()

    def generate_goto_btn(self, goto_frame, text):
        btn = tk.Button(self, text=text, command=lambda: self.controller.show_frame(goto_frame))
        btn.pack()

    def create_account(self):
        name = self._name_entry.get()
        login = self._login_entry.get()
        password = self._password_entry.get()
        user = self._user
        db = self._db
        if user.is_validated(name, login, password):
            conn = db.connect_db()
            cur = conn.cursor()
            cur.execute("""
            SELECT * FROM user WHERE user_login=?
            """, (login,))
            with conn:
                cur = conn.cursor()
                if cur.fetchall():
                    messagebox.showwarning(message=f"User with name {name} already exists")
                else:
                    cur.execute("""INSERT INTO user(user_name,user_login,user_password) VALUES(?,?,?)""",
                                (name, login, password))
                    conn.commit()
        else:
            messagebox.askyesno(title="Login error", message="Credentials failed, do you want to retry?")


