# from tkinter import *
# from tkinter import ttk
#
# root = Tk()
#
# basic_button = Button(root, text="Basic Button")
# basic_button.pack()
#
# themed_button = ttk.Button(root, text="Themed Button")
# themed_button.pack()
#
# root.mainloop()


#-----------------------------------------------------------------------------------------------------------------------
# from tkinter import *
# from tkinter import Frame
#
# root = Tk()
# frame = Frame(root)
# frame.pack()
#
# buttonframe = Frame(root)
# buttonframe.pack(side=BOTTOM)
#
# redbutton = Button(frame, text="Red", fg="red")
# redbutton.pack(side=LEFT)
#
# greenbutton = Button(frame, text="Green", fg="green")
# greenbutton.pack(side=LEFT)
#
# bluebutton = Button(frame, text="Blue", fg="blue")
# bluebutton.pack(side=LEFT)
#
# blackbutton = Button(buttonframe, text="Black", fg="black")
# blackbutton.pack(side=BOTTOM)
#
# root.mainloop()

#-----------------------------------------------------------------------------------------------------------------------
# from tkinter import *
#
# root  = Tk()
#
# for row in range(3):
#     for column in range(4):
#         label = Label(root, text="R%s/C%s"%(row,column), borderwidth=1)
#         label.grid(row=row, column=column)
#
# root.mainloop()

#-----------------------------------------------------------------------------------------------------------------------
# from tkinter import *
#
# root  = Tk()
#
# button = Button(root, text="Hi")
# button.place(x=50,y=20)
#
#
# root.mainloop()

#-----------------------------------------------------------------------------------------------------------------------

from tkinter import *

root  = Tk()
root.geometry("800x600")

b1 = Button(root, text="Hi FLAT", relief=FLAT)
b1.place(x=10,y=10)

b2 = Button(root, text="Hi RAISED", relief=RAISED)
b2.place(x=10,y=40)

b3 = Button(root, text="Hi SUNKEN", relief=SUNKEN)
b3.place(x=10,y=70)

b3 = Button(root, text="Hi SUNKEN", relief=SUNKEN, bitmap="error")
b3.place(x=10,y=100)

b3 = Button(root, text="Hi SUNKEN", relief=SUNKEN, bitmap="hourglass")
b3.place(x=10,y=130)

b3 = Button(root, text="Hi SUNKEN", relief=SUNKEN, bitmap="warning")
b3.place(x=10,y=160)

b3 = Button(root, text="Hi SUNKEN", relief=SUNKEN, bitmap="gray50")
b3.place(x=10,y=190)

b3 = Button(root, text="Hi", cursor="circle")
b3.place(x=10,y=220)

b3 = Button(root, text="Hi", cursor="plus")
b3.place(x=10,y=250)

root.mainloop()









