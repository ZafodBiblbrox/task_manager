import tkinter as tk
from tkinter import ttk
import tkcalendar as tkc
from task import Ticket
from database import SimpleDataBase
from user import User

class TaskManagerApp(tk.Frame):

    def __init__(self, master_frame, controller, db, user=None):
        super().__init__(master_frame)
        self.controller = controller
        self._db = db
        #self._db = SimpleDataBase('task_manager.db', 'task_manager_schema.txt')
        self._description_entry = None
        self._user_combobox = None
        self._closure_date = None
        self._assigned_task = None
        self._created_task = None
        self._user = user
        self._task = Ticket()
        self.execute_task_manager_gui()

    def execute_task_manager_gui(self):
        self.generate_description_section()
        self.generate_assign_section()
        self.generate_date_section()
        self.generate_submit_section()
        self.generate_task_list_section()

    def generate_description_section(self):
        frame = tk.Frame(self)
        frame.pack()

        task_label = tk.Label(frame, text="Task Description")
        task_label.pack(side=tk.LEFT)

        self._description_entry = tk.Text(frame, height=10, width=50)
        self._description_entry.pack(side=tk.LEFT)

        scroll_text = tk.Scrollbar(frame)
        scroll_text.pack(side=tk.RIGHT, fill=tk.Y)
        scroll_text.config(command=self._description_entry.yview)

        self._description_entry.config(yscrollcommand=scroll_text.set)

    def generate_assign_section(self):
        #self._db = SimpleDataBase('task_manager.db', 'task_manager_schema.txt')
        cur = self._db.connect_db().cursor()
        cur.execute("""SELECT user_login FROM user""")
        users = cur.fetchall()
        print(users)
        #registered_users = [user.login for user in self._user.users]
        frame = tk.Frame(self)
        frame.pack()

        user_label = tk.Label(frame, text="Choose user to assign: ")
        user_label.pack(side=tk.LEFT)

        self._user_combobox = ttk.Combobox(frame, values=[*users])
        self._user_combobox.pack(side=tk.LEFT)

    def generate_date_section(self):
        frame = tk.Frame(self)
        frame.pack()

        closure_date_label = tk.Label(frame, text="Choose closure date")
        closure_date_label.pack(side=tk.LEFT)

        self._closure_date = tkc.Calendar(frame, selectmode="day", year=2020, month=6, day=22)
        self._closure_date.pack(side=tk.LEFT)


    def generate_submit_section(self):
        frame = tk.Frame(self)
        frame.pack()

        submit_btn = tk.Button(frame, text="Submit task", command=self.submit_task) #command=self.submit_task
        submit_btn.pack(side=tk.LEFT)

        clear_btn = tk.Button(frame, text="Clear") #command=self.clear_task
        clear_btn.pack(side=tk.RIGHT)

    def generate_task_list_section(self):
        frame = tk.Frame(self)
        frame.pack()

        created_task_label = tk.Label(frame, text="Your created tasks")
        created_task_label.pack(side=tk.TOP)

        self._created_task = tk.Listbox(frame, selectmode=tk.MULTIPLE)
        self._created_task.pack(side=tk.RIGHT)

        assign_task_label = tk.Label(frame, text="Your assigned tasks")
        assign_task_label.pack(side=tk.RIGHT)

        self._assigned_task = tk.Listbox(frame, selectmode=tk.MULTIPLE)
        self._assigned_task.pack(side=tk.TOP)

    def submit_task(self):
        task = self._task
        task_description = self._description_entry.get("1.0", tk.END)
        closure_date = str(self._closure_date.selection_get())
        user = self._user_combobox.get()
        task.create_ticket(task_description, closure_date, user)
        open_date = str(task.open_date)
        conn = self._db.connect_db()
        cur = conn.cursor()
        print(user)
        cur.execute("""SELECT id FROM user WHERE user_login=?""", (user,))
        user_name=cur.fetchone()[0]
        print(user_name)
        cur.execute("""INSERT INTO ticket(description, open_date, closure_date, assignee_id) VALUES(?,?,?,?)""",
        (task_description, open_date, closure_date, user_name))
        conn.commit()
        self._created_task.insert(0, task)
        if task.assigned_user == user:
            self._assigned_task.insert(0, task)

