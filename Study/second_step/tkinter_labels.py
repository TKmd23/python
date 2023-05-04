import tkinter as tk

root = tk.Tk()  # Create window
root.title("TKmd test window")  # Name of window
root.geometry("600x400+400+100")
img = tk.PhotoImage(file="python.png")
label = tk.Label(root, text="Test Label1\nLabel2\nLabel3", bg="red", fg="white", font=("Arial", 18, "bold"),
                 justify='left', width=30, height=7, anchor='sw')

label.pack()
label_img = tk.Label(root, image=img)
label_img.pack()
root.mainloop()