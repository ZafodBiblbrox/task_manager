import tkinter as tk

root = tk.Tk()

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

submit_btn = tk.Button(root, text="Submit")
submit_btn.pack(side=tk.BOTTOM)

root.mainloop()