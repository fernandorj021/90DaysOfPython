from tkinter import *

def start_drawing(event):
    global last_x, last_y
    last_x, last_y = event.x, event.y


def draw(event):
    global last_x, last_y
    canvas.create_line(last_x, last_y, event.x, event.y, fill="black", width=2)
    last_x, last_y = event.x, event.y


root = Tk()


canvas = Canvas(root, width=400, height=400, bg="white")
canvas.pack()


canvas.bind("<Button-1>", start_drawing)
canvas.bind("<B1-Motion>", draw)

root.mainloop()