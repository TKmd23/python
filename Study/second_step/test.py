import tkinter as tk

root = tk.Tk()
root.geometry("600x400+300+100")

frame_menu = tk.Frame(root, bg='#1F252A', height=40)
frame_menu.pack(fill='x')

frame_text = tk.Frame(root)
frame_text.pack(fill='both', expand=True)

l_menu = tk.Label(frame_menu, text="Menu", bg="#2B3239", fg="#C6DEC1", font="Arial 10")
l_menu.place(x=10, y=10)

canvas = tk.Canvas(frame_text)
canvas.pack(side='left', fill='both', expand=True)

text = tk.Text(canvas, bg="white", fg='#C6DEC1', padx=10, pady=10, wrap='word', insertbackground="#eda756",
               selectbackground="#4e5a65", spacing3=10, width=30)
text.pack(side='left', fill='both', expand=True)

scrollbar = tk.Scrollbar(frame_text, command=canvas.yview)
scrollbar.pack(side='right', fill='y')

canvas.configure(yscrollcommand=scrollbar.set)
canvas.create_window((0,0), window=text, anchor='nw')

root.mainloop()
