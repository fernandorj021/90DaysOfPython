# from tkinter import *
#
# root = Tk()
#
# root.geometry("200x200")
#
# mb = Menubutton(root, text="Sports", relief=RAISED)
# mb.grid()
# mb.menu = Menu(mb, tearoff=0)
# mb["menu"] = mb.menu
#
# cricVar = IntVar()
# footVar = IntVar()
#
# mb.menu.add_checkbutton(label="Cricket", variable=cricVar)
# mb.menu.add_checkbutton(label="Football", variable=footVar)
#
# mb.pack()
#
# root.mainloop()

#-----------------------------------------------------------------------------------------------------------------------
# from tkinter import *
#
# root = Tk()
#
# root.geometry("200x200")
#
# menubar = Menu(root)
# filemenu = Menu(menubar,tearoff=0)
# filemenu.add_command(label="New")
# filemenu.add_command(label="Open")
# filemenu.add_command(label="Save")
# filemenu.add_command(label="Close")
# filemenu.add_separator()
# filemenu.add_command(label="Exit")
# menubar.add_cascade(label="File", menu=filemenu)
#
# editmenu = Menu(menubar,tearoff=0)
# editmenu.add_command(label="Undo")
# editmenu.add_separator()
# editmenu.add_command(label="Cut")
# editmenu.add_command(label="Copy")
# editmenu.add_command(label="Paste")
# editmenu.add_command(label="Delete")
# menubar.add_cascade(label="Edit", menu=editmenu)
#
# helpmenu = Menu(menubar,tearoff=0)
# helpmenu.add_command(label="Help Desk")
# helpmenu.add_command(label="About")
# helpmenu.add_command(label="Version Info")
# helpmenu.add_command(label="Online Help")
# menubar.add_cascade(label="Help", menu=helpmenu)
#
# root.config(menu=menubar)
#
# root.mainloop()

#-----------------------------------------------------------------------------------------------------------------------
# from tkinter import *
#
# root = Tk()
#
# root.geometry("200x200")
#
# var = StringVar()
# label = Message(root, textvariable=var,relief=RAISED)
# var.set("This is a tkinter Message Widget Tutorial")
# label.pack()
#
# root.mainloop()

#-----------------------------------------------------------------------------------------------------------------------
# from tkinter import *
#
# root = Tk()
#
# root.geometry("200x200")
#
# def sel():
#     selection = f"You have selected {str(var.get())}"
#     label.config(text = selection)
#
#
# var  = IntVar()
# R1 = Radiobutton(root, text="Option#1", variable=var, value=1, command=sel)
# R1.pack(anchor=W)
#
# R2 = Radiobutton(root, text="Option#2", variable=var, value=2, command=sel)
# R2.pack(anchor=W)
#
# R3 = Radiobutton(root, text="Option#3", variable=var, value=3, command=sel)
# R3.pack(anchor=W)
#
# R2.select()
# # R2.deselect()
#
#
# label = Label(root)
# label.pack()
#
# root.mainloop()

#-----------------------------------------------------------------------------------------------------------------------
# from tkinter import *
#
# root = Tk()
#
# root.geometry("200x200")
#
# def sel():
#
#     label.config(text=f"Value: {str(var.get())}")
#
#
# var = DoubleVar()
#
# scale = Scale(root, variable=var)
# scale.pack(anchor=CENTER)
#
#
# button = Button(root, text="Get Scale Value", command=sel)
# button.pack(anchor=CENTER)
#
# label = Label(root)
# label.pack()
#
# root.mainloop()
#-----------------------------------------------------------------------------------------------------------------------
# from tkinter import *
#
# root = Tk()
#
# root.geometry("200x200")
#
# scrollbar = Scrollbar(root)
# scrollbar.pack(side=RIGHT, fill=Y)
#
# mylist = Listbox(root,yscrollcommand=scrollbar.set)
# for line in range(100):
#     mylist.insert(END, "This is line number " + str(line))
#
# mylist.pack(side=LEFT, fill=BOTH)
# scrollbar.config(command=mylist.yview)
#
# root.mainloop()

#-----------------------------------------------------------------------------------------------------------------------
from tkinter import *

root = Tk()

root.geometry("200x200")

text = Text(root)
text.insert(INSERT, "Hello World")
text.insert(END, "Good Bye")


text.tag_add("tag","1.0", "1.5" )
text.tag_config("tag", background="black", foreground="white")

text.pack()

root.mainloop()






