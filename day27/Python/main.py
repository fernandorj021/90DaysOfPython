# from tkinter import *
#
# root = Tk()
#
# def callback():
#     print("A button was clicked!")
#
# button  = Button(root, text="Click Me", command=callback)
# button.pack()
#
# for _ in range(5):
#     button.invoke()
#
# root.mainloop()

#-----------------------------------------------------------------------------------------------------------------------
# from tkinter import *
#
# root = Tk()
#
# def callback():
#     print("A button was clicked!")
#
# button  = Button(root, text="Click Me")
# button.pack()
#
# button.config(command=callback)
#
# root.mainloop()

#-----------------------------------------------------------------------------------------------------------------------
# from tkinter import *
# from tkinter import ttk
# from turtledemo.penrose import start
#
# root = Tk()
#
# def callback():
#     print("A button was clicked!")
#
# button  = ttk.Button(root, text="Click Me")
# button.pack()
#
# button.config(command=callback)
#
# logo = PhotoImage(file="calc.gif")
# button.config(image=logo, compound=RIGHT)
# x=logo.subsample(30,30)
# button.config(image=x)
#
# button.state(["disabled"])
#
# btn_state = button.instate(["disabled"])
# print(btn_state)
#
# btn_state_2 = button.instate(["!disabled"])
# print(btn_state_2)
#
# root.mainloop()


#-----------------------------------------------------------------------------------------------------------------------
# from tkinter import *
#
# root = Tk()
#
# c = Canvas(root, bg="blue", height=250, width=300)
#
# coord = 10,50,240,210
# c.create_arc(coord,start=0, extent=150, fill="red")
#
# c.pack()
#
# root.mainloop()

#-----------------------------------------------------------------------------------------------------------------------
# from tkinter import *
#
# root = Tk()
#
# c = Canvas(root, bg="blue", height=250, width=300)
#
# c.create_line(108,120,320,40, fill="red")
# c.create_oval(80,30,140,150, fill="green")
#
# c.pack()
#
# root.mainloop()

#-----------------------------------------------------------------------------------------------------------------------
# from tkinter import *
#
# root = Tk()
#
# root.geometry("1000x1000")
#
# chkbtnStatus = BooleanVar()
# chkbtnStatus.set(True)
#
# def func():
#     print("Check Box")
#
# chkbtn = Checkbutton(root, text="check box", var = chkbtnStatus, command=func)
#
# chkbtn.grid(column=0, row=0)
#
# chkbtn.deselect()
# chkbtn.toggle()
#
# chkbtn.select()
# chkbtn.toggle()
#
# root.mainloop()

#-----------------------------------------------------------------------------------------------------------------------
# from tkinter import *
#
# root = Tk()
#
# root.geometry("200x200")
#
# label1 = Label(root, text="Username")
# label1.pack(side=LEFT)
#
# entry1 = Entry(root, bd=5)
# entry1.pack(side=RIGHT)
# entry1.insert(0, "Enter Something")
# entry1.delete(0,6)
# s = entry1.get()
# print(s)
#
# root.mainloop()

#-----------------------------------------------------------------------------------------------------------------------
# from tkinter import *
#
# root = Tk()
#
# root.geometry("200x200")
#
# label1 = Label(root, text="Password")
# label1.pack(side=LEFT)
#
# entry1 = Entry(root, bd=5, show="*")
# entry1.pack(side=RIGHT)
# entry1.insert(0, "Enter Something")
# entry1.delete(0,6)
# s = entry1.get()
# print(s)
#
# root.mainloop()

#-----------------------------------------------------------------------------------------------------------------------
from tkinter import *

root = Tk()

root.geometry("200x200")

lb = Listbox(root)
lb.insert(1, "Python")
lb.insert(3, "C")
lb.insert(2, "Ruby")

lb.insert(END, "Pearl")

# lb.delete(0,2)

print(lb.size())

lb.pack()

root.mainloop()




