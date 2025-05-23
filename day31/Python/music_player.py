from tkinter import *
from tkinter import filedialog
import tkinter.messagebox
from pygame import mixer



window = Tk()
mixer.init()

window.geometry("300x300")
window.title("Python Music Player")

def browse_file():
    global filename
    filename = filedialog.askopenfilename()

def help_me():
    tkinter.messagebox.showinfo("Help", "How amazing it is")


menubar = Menu(window)

window.config(menu=menubar)

submenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label="File", menu=submenu)
submenu.add_command(label="Open", command=browse_file)
submenu.add_command(label="Exit", command=window.destroy)

submenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label="About Us", menu=submenu)
submenu.add_command(label="Help", command=help_me)
submenu.add_command(label="Exit")

text_label = Label(window, text="This is a Play Button")
text_label.pack()

def play_music():
    try:
        paused
    except:
        try:
            mixer.music.load(filename)
            mixer.music.play()
            statusbar['text'] = "Music is playing"
        except:
            tkinter.messagebox.showerror("Error", "File Not Found")
            print("File Not Found")
    else:
        mixer.music.unpause()
        statusbar['text'] = "Music is resumed"

def stop_music():
    mixer.music.stop()
    statusbar['text'] = "Music is stopped"

def pause_music():
    global paused
    paused = True
    mixer.music.pause()
    statusbar['text'] = "Music is paused"

def rewind_music():
    play_music()
    statusbar['text'] = "Music is rewind"


def set_volume(value):
    volume_v = int(value) / 100
    mixer.music.set_volume(volume_v)

frame = Frame(window)
frame.pack(padx=10, pady=10)

play_button = Button(frame, text="Play", command=play_music)
play_button.grid(row=0, column=0, padx=10)

pause_button = Button(frame, text="Pause", command=pause_music)
pause_button.grid(row=0, column=1, padx=10)

stop_button = Button(frame, text="Stop", command=stop_music)
stop_button.grid(row=0, column=2, padx=10)

bottomframe = Frame(window)
bottomframe.pack()

rewind_button = Button(bottomframe, text="Rewind", command=rewind_music)
rewind_button.grid(row=0, column=0, padx=10)

volume = Scale(bottomframe, orient=HORIZONTAL, from_=0, to=100, command=set_volume)
volume.set(70)
volume.grid(row=0, column=1)

statusbar = Label(window,text="Keep enjoying the music", relief=SUNKEN, anchor=W)
statusbar.pack(side=BOTTOM, fill=X)

window.mainloop()