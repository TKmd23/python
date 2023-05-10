import tkinter as tk

root = tk.Tk()
root.geometry("600x400+400+100")

# f_top = tk.LabelFrame(root, text="Top frame", padx=10)
# f_top.pack(pady=10)
# f_bottom = tk.Frame(root)
# f_bottom.pack()
#
# lab = tk.Label(f_top, text="1", font="15", fg="black", bg="red", width=8, height=4).pack(side="left")
# lab1 = tk.Label(f_top, text="2", font="15", fg="black", bg="green", width=8, height=4).pack(side='left')
# lab2 = tk.Label(f_bottom, text="3", font="15", fg="black", bg="blue", width=8, height=4).pack(side='left')
# lab3 = tk.Label(f_bottom, text="4", font="15", fg="black", bg="yellow", width=8, height=4).pack(side='left')
lab4 = tk.Label(root, text="4", font="15", fg="black", bg="yellow", width=8, height=4).pack(anchor='w', expand=1)


# btn = tk.Button(root)
# # btn.pack()

root.mainloop()
