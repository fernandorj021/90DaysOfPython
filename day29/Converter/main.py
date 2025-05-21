from tkinter import *

def converter():
    option = selected_option.get()
    if option == 0:
        F = entry_temp.get()
        C = (F-32.0) * (5/9)
        result.set(f"{F}F = {C}C")
    else:
        C = entry_temp.get()
        F = C * (9/5) + 32
        result.set(f"{C}C = {F}F")

root = Tk()
root.title("Temperature Converter Application")
root.geometry("470x150")

entry_temp = DoubleVar()
entry = Entry(root, textvariable=entry_temp)
entry.grid(row=0, column=0, padx=10, sticky="nsew")

btn_converter = Button(root, text="Convert", command=converter)
btn_converter.grid(row=0,column=1, padx=10, sticky="nsew")

result = StringVar()
result.set("")
result_label = Label(root, textvariable=result)
result_label.grid(row=0,column=2, sticky="nsew")

selected_option = IntVar()
selected_option.set(0)
rb1 = Radiobutton(root, variable=selected_option, text="Fahrenheit to Celsius", value=0)
rb1.grid(row=1,column=0)

rb2 = Radiobutton(root, variable=selected_option, text="Celsius to Fahrenheit", value=1)
rb2.grid(row=2,column=0)

root.mainloop()