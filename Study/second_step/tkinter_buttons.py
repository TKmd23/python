import tkinter as tk
import time

root = tk.Tk()  # Create window
root.title("TKmd test window")  # Name of window
root.iconbitmap("logo.ico")  # Logo image left corner
root.geometry("600x400+400+100")  # Size of window and spawn point
root.resizable(False, False)  # Block resize
root.config(bg="#88b5b2")  # BG color


# Button
def check_time():
    btn_time['text'] = time.strftime("%H:%M:%S")


counter = 0


def check_count():
    global counter
    counter += 1
    root.title(f"Counter: {counter}")


btn_time = tk.Button(root, text="Timer", command=check_time)
btn_time.pack()

btn_cnt = tk.Button(root, text="Clicker", command=check_count)
btn_cnt.pack()

root.mainloop()
