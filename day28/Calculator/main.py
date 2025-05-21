from tkinter import *

expression = ""

def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)

def equalpress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression=""

    except:
        equation.set("error generated")
        expression=""

def clear():
    global expression
    expression = ""
    equation.set("")



if __name__ == "__main__":
    root = Tk()
    root.configure(background="grey")
    root.title("Calculator Application")
    root.geometry("270x150")

    equation = StringVar()

    expression_field = Entry(root, textvariable=equation)
    expression_field.grid(columnspan=4, ipadx=70)

    equation.set("Enter your expression")

    button1 = Button(root, text= " 1 ", fg="white", bg="black", command=lambda : press(1), height=1, width=7)
    button1.grid(row=2,column=0)

    button2 = Button(root, text=" 2 ", fg="white", bg="black", command=lambda: press(2), height=1, width=7)
    button2.grid(row=2, column=1)

    button3 = Button(root, text=" 3 ", fg="white", bg="black", command=lambda: press(3), height=1, width=7)
    button3.grid(row=2, column=2)

    button4 = Button(root, text=" 4 ", fg="white", bg="black", command=lambda: press(4), height=1, width=7)
    button4.grid(row=3, column=0)

    button5 = Button(root, text=" 5 ", fg="white", bg="black", command=lambda: press(5), height=1, width=7)
    button5.grid(row=3, column=1)

    button6 = Button(root, text=" 6 ", fg="white", bg="black", command=lambda: press(6), height=1, width=7)
    button6.grid(row=3, column=2)

    button7 = Button(root, text=" 7 ", fg="white", bg="black", command=lambda: press(7), height=1, width=7)
    button7.grid(row=4, column=0)

    button8 = Button(root, text=" 8 ", fg="white", bg="black", command=lambda: press(8), height=1, width=7)
    button8.grid(row=4, column=1)

    button9 = Button(root, text=" 9 ", fg="white", bg="black", command=lambda: press(9), height=1, width=7)
    button9.grid(row=4, column=2)

    # button0 = Button(root, text=" 0 ", fg="white", bg="black", command=lambda: press(0), height=1, width=7)
    # button0.grid(row=5, column=0)


    button_add = Button(root, text=" + ", fg="white", bg="black", command=lambda: press("+"), height=1, width=7)
    button_add.grid(row=2, column=3)


    button_subtract = Button(root, text=" - ", fg="white", bg="black", command=lambda: press("-"), height=1, width=7)
    button_subtract.grid(row=3, column=3)


    button_multiply = Button(root, text=" × ", fg="white", bg="black", command=lambda: press("*"), height=1, width=7)
    button_multiply.grid(row=4, column=3)


    button_divide = Button(root, text=" ÷ ", fg="white", bg="black", command=lambda: press("/"), height=1, width=7)
    button_divide.grid(row=5, column=3)


    button_equal = Button(root, text=" = ", fg="white", bg="black", command=lambda: equalpress(), height=1, width=7)
    button_equal.grid(row=5, column=2)


    button_clear = Button(root, text=" C ", fg="white", bg="black", command=lambda: clear(), height=1, width=7)
    button_clear.grid(row=5, column=0)


    button_zero = Button(root, text=" 0 ", fg="white", bg="black", command=lambda: press(0), height=1, width=7)
    button_zero.grid(row=5, column=1)

    Decimal = Button(root, text=" . ", fg="white", bg="black", command=lambda: press("."), height=1, width=7)
    Decimal.grid(row=6, column=0)



    root.mainloop()