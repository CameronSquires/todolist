from tkinter import *
from tkinter import messagebox
import pickle

root = Tk()
root.title("TODO")

itemFrame = Frame(root, width=50)
itemFrame.pack(side=TOP)

def addTodo():
    if todoEntry.get() == "":
        messagebox.showwarning(title="WARNING", message="Please input a valid argument.")
    else:
        item = todoEntry.get()
        todoList.insert(END, item)
        todoEntry.delete(0, END)

def deleteTodo():
    try:
        selItem = todoList.curselection()[0]
        todoList.delete(selItem)
    except:
        messagebox.showerror(title="ERROR", message="You need to select an item to delete.")

def saveTodo():
    allTasks = todoList.get(0, todoList.size())
    pickle.dump(allTasks, open("todoitems.dat", "wb"))


def loadTodo():
    try:
        allTasks = pickle.load(open("todoitems.dat", "rb"))
        todoList.delete(0, END)
        for item in allTasks:
            todoList.insert(END, item)
    except:
        messagebox.showerror(title="ERROR", message="No Data File Specified.")
def clearTodo():
    todoList.delete(0, END)

def exit():
    root.destroy()


todoList = Listbox(itemFrame, height=5, width=48)
todoList.pack(side=LEFT)

listScroll = Scrollbar(itemFrame, width=20)
listScroll.pack(side=RIGHT, fill=Y)

todoList.config(yscrollcommand=listScroll.set)
listScroll.config(command=todoList.yview)

todoEntry = Entry(root, width=52)
todoEntry.pack()



addTaskBtn = Button(root, text="Add Task", width=48, command=addTodo)
addTaskBtn.pack()

delTaskBtn = Button(root, text="Delete Task", width=48, command=deleteTodo)
delTaskBtn.pack()

saveTaskBtn = Button(root, text="Save Tasks", width=48, command=saveTodo)
saveTaskBtn.pack()

loadTaskBtn = Button(root, text="Load Tasks", width=48, command=loadTodo)
loadTaskBtn.pack()

delTaskBtn = Button(root, text="Clear All Tasks", width=48, command=clearTodo)
delTaskBtn.pack()

exitBtn = Button(root, text="EXIT", width=48, command=exit)
exitBtn.pack()



root.mainloop()