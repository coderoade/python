from tkinter import *

class ToDoList:
    def __init__(self, root):
        self.tasks = []
        self.root = root
        self.listbox = Listbox(self.root)
        self.entry = Entry(self.root)
        self.addButton = Button(self.root, text="add the task by clicking me", command=self.add_task)
        self.delButton = Button(self.root, text="Delete Task by clicking me", command=self.delete_task)

        # GUI Layout
        self.entry.pack()
        self.addButton.pack()
        self.listbox.pack()
        self.delButton.pack()

    def add_task(self):
        task = self.entry.get()
        if task != "":
            self.listbox.insert(END, task)
            self.entry.delete(0, END)

    def delete_task(self):
        try:
            task_index = self.listbox.curselection()[0]
            self.listbox.delete(task_index)
        except:
            pass

root = Tk()
root.title("Python To-Do List")
root.geometry("350x450") 
to_do_list = ToDoList(root)
root.mainloop()