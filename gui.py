import tkinter as tk
from tkinter import ttk
import tkcalendar as tkc

root = tk.Tk()

#Task Description section
task_description_frame = tk.Frame(root)
task_description_frame.pack()

task_label = tk.Label(task_description_frame, text='Task Description')
task_label.pack(side=tk.LEFT)

task_description = tk.Text(task_description_frame, height=10, width=50)
task_description.pack(side=tk.LEFT)

scroll_text = tk.Scrollbar(task_description_frame)
scroll_text.pack(side=tk.RIGHT, fill=tk.Y)
scroll_text.config(command=task_description.yview)
task_description.config(yscrollcommand=scroll_text.set)

#Assign user section
assign_user_frame = tk.Frame(root)
assign_user_frame.pack()

user_label = tk.Label(assign_user_frame, text="Choose user to assign: ")
user_label.pack(side=tk.LEFT)

user_combobox = ttk.Combobox(assign_user_frame, values=["User1", "User2", "User3", "User4", "User5"])
user_combobox.pack(side=tk.LEFT)

#Closure date section
calendar_frame = tk.Frame(root)
calendar_frame.pack()

closure_date_label = tk.Label(calendar_frame, text="Choose closure date")
closure_date_label.pack(side=tk.LEFT)

closure_date_picker = tkc.Calendar(calendar_frame, selectmode="day", year=2020, month=5, day=22)
closure_date_picker.pack(side=tk.LEFT)

closure_date_btn = tk.Button(calendar_frame, text="Submit date")
closure_date_btn.pack(side=tk.BOTTOM)

#Submit task section
submit_frame = tk.Frame(root)
submit_frame.pack()

submit_btn = tk.Button(submit_frame, text="Submit task")
submit_btn.pack(side=tk.LEFT)

cancel_btn = tk.Button(submit_frame, text="Cancel")
cancel_btn.pack(side=tk.RIGHT)

#Task list section
task_frame = tk.Frame(root)
task_frame.pack()

created_task_label = tk.Label(task_frame, text="Your created tasks")
created_task_label.pack(side=tk.TOP)

created_tasks = tk.Listbox(task_frame, selectmode=tk.MULTIPLE)
created_tasks.pack(side=tk.LEFT)

assign_task_label = tk.Label(task_frame, text="Your assigned task")
assign_task_label.pack(side=tk.TOP)

assinged_tasks = tk.Listbox(task_frame, selectmode=tk.MULTIPLE)
assinged_tasks.pack(side=tk.RIGHT)

root.mainloop()