import tkinter as tk
from user import User

user = User()


def get_user_cerdentials():
    name = name_entry.get()
    login = login_entry.get()
    password = password_entry.get()
    user.log_in_system(name, login, password)
    print(user.name)
    print(user.login)
    print(user.password)
    print(user.authorized)


root = tk.Tk()

name_frame = tk.Frame(root)
name_frame.pack()

name_label = tk.Label(name_frame, text="Enter your name")
name_label.pack(side=tk.LEFT)

name_entry = tk.Entry(name_frame)
name_entry.pack(side=tk.RIGHT)

login_frame = tk.Frame(root)
login_frame.pack()

login_label = tk.Label(login_frame, text="Enter your login")
login_label.pack(side=tk.LEFT)

login_entry = tk.Entry(login_frame)
login_entry.pack(side=tk.RIGHT)

password_frame = tk.Frame(root)
password_frame.pack()

password_label = tk.Label(password_frame, text="Enter your password")
password_label.pack(side=tk.LEFT)

password_entry = tk.Entry(password_frame)
password_entry.pack(side=tk.RIGHT)

submit_btn = tk.Button(root, text="Submit", command=get_user_cerdentials)
submit_btn.pack(side=tk.BOTTOM)

root.mainloop()

