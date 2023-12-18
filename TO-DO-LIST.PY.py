from tkinter import *
from tkinter import messagebox


def newTask():
    task = my_entry.get()
    if task != "":
        lb.insert(END, task)
        my_entry.delete(0, "end")
    else:
        messagebox.showwarning("warning", "please enter some task")


def deleteTask():
    lb.delete(ANCHOR)


ws = Tk()
ws.title("TO-DO-LIST APP")
ws.geometry('500x450')
ws.config(bg='antiquewhite')
ws.resizable(width=False, height=False)

# frame
frame = Frame(ws)
frame.pack(pady=10)

# listbox
lb = Listbox(frame, width=25, height=8, font=['Times', 18], bd=0, fg='#464646', highlightthickness=0,
             selectbackground='#a6a6a6',
             activestyle="none"
             )
lb.pack(side=LEFT, fill=BOTH)

# task list

task_list = ['HP', 'DELL', 'LENOVO', 'ACER', 'SAMSUNG']

for item in task_list:
    lb.insert(END, item)

# scrollbar

sb = Scrollbar(frame)
sb.pack(side=RIGHT, fill=BOTH)

lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)
my_entry = Entry(ws, font=('Times', 24))
my_entry.pack(pady=20)

# buttons
button_frame = Frame(ws)
button_frame.pack(pady=20)

# addtask
addTask_btn = Button(
    button_frame,
    text='Add task',
    font=('Times 14'),
    bg='#c5f776',
    padx=20,
    pady=10,
    command=newTask)

addTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

# del task
delTask_btn = Button(
    button_frame,
    text='delete task',
    font=('Times 14'),
    bg='#ff8b61',
    padx=20,
    pady=10,
    command=deleteTask)

delTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

ws.mainloop()