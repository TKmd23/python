from tkinter import *
import time

root = Tk()

def tick():
    clock.after(400, tick)
    clock['text'] = time.strftime('%H:%M:%S')

clock = Label(root, font=("Comic Sans MS", 50))
clock.pack()

tick()

root.mainloop()
