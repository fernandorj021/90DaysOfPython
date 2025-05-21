from tkinter import *

def add():
    todo_item = todo_field.get()
    todo_list.insert(END, todo_item)
    entry_var.set("")

def remove():
    selected = todo_list.curselection()
    todo_list.delete(selected)

root = Tk()
root.title("To-Do List")
root.geometry("500x500")

label = Label(root, text="Enter an item to add: ")
label.grid(row=0, column=0, padx=5, pady=5)

entry_var = StringVar()
todo_field = Entry(root, textvariable=entry_var ,width=30)
todo_field.grid(row=0, column=1, padx=5, pady=5)

button_add = Button(root, text="Add", command=add)
button_add.grid(row=0, column=2, padx=5, pady=5)

button_remove = Button(root, text="Remove", command=remove)
button_remove.grid(row=0, column=3, padx=5, pady=5)


todo_list = Listbox(root, width=30)
todo_list.grid(row=1, column=1)

root.mainloop()