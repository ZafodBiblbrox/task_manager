import tkinter as tk
from database import SimpleDataBase
from initial_window import InitialWindow


class ControllerWindow(tk.Tk):

    def __init__(self):
        super().__init__()
        container_frame = tk.Frame(self)
        container_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        container_frame.grid_rowconfigure(0, weight=1)
        container_frame.grid_columnconfigure(0, weight=1)
        self._db = SimpleDataBase('task_manager.db', 'task_manager_schema.txt')
        self.slave = self.slave_generator(master=container_frame, controller=self, db=self._db)
        self.slave.send(None)
        self.show_frame(InitialWindow)

    def slave_generator(self, master, controller, db):
        return_value = None
        while True:
            SlaveClass = yield return_value
            slave_frame = SlaveClass(master, controller, db)
            slave_frame.grid(row=0, column=0, sticky="nsew")
            return_value = slave_frame

    def show_frame(self, frame_name):
        frame = self.slave.send(frame_name)
        frame.tkraise()


controller = ControllerWindow()
controller.mainloop()
