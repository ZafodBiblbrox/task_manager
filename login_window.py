import tkinter as tk
from tkinter import messagebox
import gui
import initial_window
from gui import TaskManagerApp
from database import SimpleDataBase


class LoginWindowApp(tk.Frame):

    def __init__(self, master_frame, controller, db):
        super().__init__(master_frame)
        self.controller = controller
        #self._db = SimpleDataBase('task_manager.db', 'task_manager_schema.txt')
        self._db = db
        self._login_entry = None
        self._password_entry = None
        self.execute_window()

    def execute_window(self):
        self.generate_login_section()
        self.generate_password_section()
        self.generate_submit_btn()
        self.generate_goto_btn(initial_window.InitialWindow, text='Back to initial')

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

        submit_btn = tk.Button(self, text='Login', command=self.log_in)
        submit_btn.pack()

    def generate_goto_btn(self, goto_frame, text):
        btn = tk.Button(self, text=text, command=lambda: self.controller.show_frame(goto_frame))
        btn.pack()

    def log_in(self):
        login = self._login_entry.get()
        suggested_password = self._password_entry.get()

        db = self._db
        with db.connect_db() as conn:
            cur = conn.cursor()
            cur.execute("""
                        SELECT user_password
                        FROM user
                        WHERE user_login=?
                        """, (login,))

            user_password = cur.fetchone()[0]
            if user_password != suggested_password:
                messagebox.showerror(title='Access denied', message='Wrong login or password')
            else:
                #self.controller.show_frame('TaskManagerApp')
                self.controller.show_frame(gui.TaskManagerApp)
