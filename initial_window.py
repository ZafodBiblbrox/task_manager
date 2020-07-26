import tkinter as tk
#from login_window import LoginWindowApp
import account
import login_window

class InitialWindow(tk.Frame):

    def __init__(self, master_frame, controller, db):
        super().__init__(master_frame)
        self.controller = controller
        self.execute_window()

    def execute_window(self):
        self.generate_label('Create account or login')
        self.generate_btn(text="I have account", func=self.controller.show_frame, params=login_window.LoginWindowApp)
        self.generate_btn(text="Create account", func=self.controller.show_frame, params=account.Account)

    def generate_btn(self, text, func, params=None):
        btn = tk.Button(self, text=text, command=lambda: func(params))
        btn.pack()

    def generate_label(self, text):
        label = tk.Label(self, text=text)
        label.pack(side="top", fill="x", pady=10)
