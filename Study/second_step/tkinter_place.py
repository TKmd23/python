import tkinter as tk


root = tk.Tk()
root.geometry("400x400+400+100")

# label1 = tk.Label(root, text="Hello!", bg='green', fg="white", font=16, padx=20, pady=8)
# label1.place(x=0, y=0)
#
# label2 = tk.Label(root, text="Hello!", bg='green', fg="white", font=16, padx=20, pady=8)
# label2.place(relx=0.5, rely=0.5, anchor="center")
label = tk.Label(root, bg="black")
label.place(relx=0.5, rely=0.5, anchor="center", relheight=0.8, relwidth=0.8)

label2 = tk.Label(root, text="Hello!", bg='green', fg="white", font=16, padx=20, pady=8)
label2.place(relx=0.5, rely=0.5, anchor="center")

root.mainloop()
