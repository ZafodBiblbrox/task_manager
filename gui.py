import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
task_description = tk.Text(root, height=10, width=50)
task_label = tk.Label(root, text='Task Description')
task_label.pack(side=tk.LEFT)
task_description.pack(side=tk.LEFT)
scroll_text = tk.Scrollbar(root)
scroll_text.pack(side=tk.RIGHT, fill=tk.Y)
scroll_text.config(command=task_description.yview)
task_description.config(yscrollcommand=scroll_text.set)


root.mainloop()
