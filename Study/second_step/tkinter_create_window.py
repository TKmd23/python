import tkinter as tk

root = tk.Tk()  # Create window
root.title("TKmd test window")  # Name of window
root.iconbitmap("logo.ico")  # Logo image left corner
root.geometry("600x400+400+100")  # Size of window and spawn point
root.resizable(False, False)  # Block resize
root.config(bg="#88b5b2")  # BG color


# Button

def button_click():
    print("Click!!!")


btn = tk.Button(root, text="Main\nbutton", bd=20, command=button_click, font=("Comic Sans MS", 20, "bold"),
                justify="left", relief='ridge', activebackground="blue", activeforeground="red", fg='green', bg='yellow',
                highlightcolor='pink', padx=10)
# btn.configure(width=20, height=5)
# btn['font'] = "Arial"
btn.pack()

root.mainloop()
