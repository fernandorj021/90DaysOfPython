from importlib.metadata import entry_points
from tkinter import *

expression = ""

def press(num_op):
    global expression
    expression = expression + str(num_op)
    equation.set(expression)


def calculate():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = ""

    except:
        equation.set("error generated")
        expression = ""

root = Tk()
root.configure(background="grey")
root.title("Calculator Application")
root.geometry("270x150")

equation = StringVar()
equation.set("0")

field = Entry(root, textvariable=equation)
field.grid(columnspan=4, ipadx=70)

btn7 = Button(root, text="7", fg="white", bg="black", command= lambda : press(7), height=1, width=7)
btn7.grid(row=1,column=0)

btn8 = Button(root, text="8", fg="white", bg="black", command= lambda : press(8), height=1, width=7)
btn8.grid(row=1,column=1)

btn9 = Button(root, text="9", fg="white", bg="black", command= lambda : press(9), height=1, width=7)
btn9.grid(row=1,column=2)

btn_mult = Button(root, text="X", fg="white", bg="black", command= lambda : press(7), height=1, width=7)
btn_mult.grid(row=1,column=3)

btn4 = Button(root, text="4", fg="white", bg="black", command=lambda: press(4), height=1, width=7)
btn4.grid(row=2, column=0)

btn5 = Button(root, text="5", fg="white", bg="black", command=lambda: press(5), height=1, width=7)
btn5.grid(row=2, column=1)

btn6 = Button(root, text="6", fg="white", bg="black", command=lambda: press(6), height=1, width=7)
btn6.grid(row=2, column=2)

btn_sub = Button(root, text="-", fg="white", bg="black", command=lambda: press('-'), height=1, width=7)
btn_sub.grid(row=2, column=3)

btn1 = Button(root, text="1", fg="white", bg="black", command=lambda: press(1), height=1, width=7)
btn1.grid(row=3, column=0)

btn2 = Button(root, text="2", fg="white", bg="black", command=lambda: press(2), height=1, width=7)
btn2.grid(row=3, column=1)

btn3 = Button(root, text="3", fg="white", bg="black", command=lambda: press(3), height=1, width=7)
btn3.grid(row=3, column=2)

btn_add = Button(root, text="+", fg="white", bg="black", command=lambda: press('+'), height=1, width=7)
btn_add.grid(row=3, column=3)

btn0 = Button(root, text="0", fg="white", bg="black", command=lambda: press(0), height=1, width=7)
btn0.grid(row=4, column=0)

btn_dot = Button(root, text=".", fg="white", bg="black", command=lambda: press('.'), height=1, width=7)
btn_dot.grid(row=4, column=1)

btn_equal = Button(root, text="=", fg="white", bg="black", command=lambda: calculate(), height=1, width=7)
btn_equal.grid(row=4, column=2)

btn_div = Button(root, text="/", fg="white", bg="black", command=lambda: press('/'), height=1, width=7)
btn_div.grid(row=4, column=3)

root.mainloop()