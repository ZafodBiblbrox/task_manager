import tkinter as tk
from user import User

class LoginWindowApp(tk.Frame):

    root = tk.Tk()

    def __init__(self, master=root):
        super().__init__(master)
        #self._user = user
        self._name_entry = None
        self._login_entry = None
        self._password_entry = None
        self.pack()
        self.execute_login_window()

    @property
    def name_entry(self):
        return self._name_entry

    @name_entry.setter
    def name_entry(self, entry):
        self._name_entry = entry

    @property
    def login_entry(self):
        return self._login_entry

    @property
    def password_entry(self):
        return self._password_entry


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

        name_entry = tk.Entry(frame)
        name_entry.pack(side=tk.LEFT)
        

    def generate_login_section(self):
        frame = tk.Frame(self)
        frame.pack()

        login_label = tk.Label(frame, text="Enter your login")
        login_label.pack(side=tk.LEFT)

        login_entry = tk.Entry(frame)
        self._login_entry = login_entry.get()
        login_entry.pack(side=tk.LEFT)

    def generate_password_section(self):
        frame = tk.Frame(self)
        frame.pack()

        password_label = tk.Label(frame, text="Enter your password")
        password_label.pack(side=tk.LEFT)

        password_entry = tk.Entry(frame)
        self._password_entry = password_entry.get()
        password_entry.pack(side=tk.LEFT)

    def generate_submit_btn(self):
        frame=tk.Frame(self)
        frame.pack()

        submit_btn = tk.Button(self, text='Login', command=self.print_data)
        submit_btn.pack(side=tk.BOTTOM)

    def print_data(self):
        print(self.name_entry)
        print(self.login_entry)
        print(self.password_entry)

lw = LoginWindowApp()

lw.mainloop()