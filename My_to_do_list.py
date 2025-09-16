from tkinter import *

root = Tk()
root.title("My To-Do List")
root.geometry("400x500")
root.minsize(400,500)
root.maxsize(400,500)
root.config(bg="lightblue")


def win_red():
    root.config(bg='red')
def win_yellow():
    root.config(bg='yellow')
def win_blue():
    root.config(bg='blue')
def win_green():
    root.config(bg='green')
def win_lightblue():
    root.config(bg='lightblue')

def add_task():

    x = task_entry.get()
    if task_entry.get() != '':
        listbox.insert(END , x)
        task_entry.delete(0,END)

def delete_task():
    listbox.delete(ANCHOR)

def clear():
    listbox.delete(0,END)

my_menu = Menu()
root.config(menu=my_menu )

win_Theme = Menu(my_menu)
my_menu.add_cascade(label='Theme',menu=win_Theme)
win_Theme.add_cascade(label='Red',command=win_red)
win_Theme.add_cascade(label='Yellow',command=win_yellow)
win_Theme.add_cascade(label='Blue',command= win_blue)
win_Theme.add_cascade(label='green',command= win_green)
win_Theme.add_cascade(label='lightblue',command= win_lightblue)




Label(root, text="My To-Do List", font=("Arial", 20, "bold"), bg="lightblue").pack(pady=10)

# Entry for new task
task_entry = Entry(root, width=30, font=("Arial", 14) , bd=5)
task_entry.pack(pady=10)

# Buttons
frame = Frame(root)
frame.pack(pady=10)

add_button = Button(frame, text="Add Task", width=12, command=add_task)
add_button.grid(row=0, column=0, padx=5)

delete_button = Button(frame, text="Delete Selected", width=12, command=delete_task)
delete_button.grid(row=0, column=1, padx=5)

clear_button = Button(frame, text="Clear All", width=12,command=clear )
clear_button.grid(row=0, column=2, padx=5)

scbar = Scrollbar()

# Listbox to show tasks
listbox = Listbox(root, width=45, height=18, font=("Arial", 12), selectbackground="gray", selectforeground="white" ,yscrollcommand=Y)
listbox.pack(pady=20)

# Run the main loop
root.mainloop()


