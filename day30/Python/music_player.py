from tkinter import *
from pygame import mixer

window = Tk()
mixer.init()

window.geometry("300x300")
window.title("Python Music Player")

text_label = Label(window, text="This is a Play Button")
text_label.pack()

def play_music():
    mixer.music.load("jazz.mp3")
    mixer.music.play()

def stop_music():
    mixer.music.stop()

def set_volume(value):
    print(value)
    volume_v = int(value) / 100
    mixer.music.set_volume(volume_v)

# photo = PhotoImage(file="play.png",width=100, height=100)
play_button = Button(window, text="Play", command=play_music)
play_button.pack()

stop_button = Button(window, text="Stop", command=stop_music)
stop_button.pack()

volume = Scale(window, orient=HORIZONTAL, from_=0, to=100, command=set_volume)
volume.set(70)
volume.pack()

window.mainloop()