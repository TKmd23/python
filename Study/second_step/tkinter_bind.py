from tkinter import *

root = Tk()
root.geometry("500x500+400+100")

def lab_event(event, key):
    if key == "Left click":
        print("Left click")
    elif key == "Middle click":
        print("Middle click")
    elif key == "Right click":
        print("Right click")


e = Entry(root, justify='center', font="Arial 15")
e.pack(fill="x", expand=True, padx=15, ipady=5)
e.bind("<Button-1>", lambda event, key="Left click": lab_event(event, key))
e.bind("<Button-2>", lambda event, key="Middle click": lab_event(event, key))
e.bind("<Button-3>", lambda event, key="Right click": lab_event(event, key))

root.mainloop()
