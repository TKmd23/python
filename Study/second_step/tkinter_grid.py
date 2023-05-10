import tkinter as tk

root = tk.Tk()
# root.geometry("600x400+400+100")

# f = tk.Frame(root)
# f.pack(pady=10)
#
# btn7 = tk.Button(f, text="7", padx=10, pady=5).grid(row=0, column=0)
# btn8 = tk.Button(f, text="8", padx=10, pady=5).grid(row=0, column=1)
# btn9 = tk.Button(f, text="9", padx=10, pady=5).grid(row=0, column=2)
# btn4 = tk.Button(f, text="4", padx=10, pady=5).grid(row=1, column=0)
# btn5 = tk.Button(f, text="5", padx=10, pady=5).grid(row=1, column=1)
# btn6 = tk.Button(f, text="6", padx=10, pady=5).grid(row=1, column=2)
# btn1 = tk.Button(f, text="1", padx=10, pady=5).grid(row=2, column=0)
# btn2 = tk.Button(f, text="2", padx=10, pady=5).grid(row=2, column=1)
# btn3 = tk.Button(f, text="3", padx=10, pady=5).grid(row=2, column=2)
# btn0 = tk.Button(f, text="0", padx=10, pady=5).grid(row=3, column=1)

l_label = tk.Label(root, text="Login: ").grid(row=0, column=0, padx=10, pady=10, sticky='w')
l_enter = tk.Entry(root).grid(row=0, column=1, columnspan=2, padx=10, pady=10, sticky="we")

p_label = tk.Label(root, text="Password: ").grid(row=1, column=0, padx=10, pady=10, sticky='w')
p_enter = tk.Entry(root, show='*').grid(row=1, column=1, columnspan=2, padx=10, pady=10, sticky="we")

btn_enter = tk.Button(root, text="Login", padx=5).grid(row=2, column=0, pady=10)
btn_forgot = tk.Button(root, text="Forgot pass", padx=5).grid(row=2, column=1, pady=10)
btn_exit = tk.Button(root, text="Exit", padx=5).grid(row=2, column=2, pady=10)

root.mainloop()
