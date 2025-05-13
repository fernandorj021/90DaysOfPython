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
from tkinter import *

root  = Tk()

button = Button(root, text="Hi")
button.place(x=50,y=20)


root.mainloop()




