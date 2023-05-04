import tkinter as tk

root = tk.Tk()
dicter = {"red": "Красный",
          "orange": "Оранжевый",
          "yellow": "Желтый",
          "green": "Зеленый",
          "lightblue": "Голубой",
          "blue": "Синий",
          "violet": "Фиолетовый"}

def check_color(event):
    color = event.widget["bg"]
    label['text'] = f"Color: {color}"
    enter.delete(0, 'end')
    enter.insert(0, dicter[color])




label = tk.Label(root, text="Color: ")
label.pack()
enter = tk.Entry(root, width=30, justify='center')
enter.pack()
btn_1 = tk.Button(root, bg='red')
btn_1.bind("<Button-1>", check_color)
btn_1.pack(fill='x')
btn_2 = tk.Button(root, bg='orange')
btn_2.bind("<Button-1>", check_color)
btn_2.pack(fill='x')
btn_3 = tk.Button(root, bg='yellow')
btn_3.bind("<Button-1>", check_color)
btn_3.pack(fill='x')
btn_4 = tk.Button(root, bg='green')
btn_4.bind("<Button-1>", check_color)
btn_4.pack(fill='x')
btn_5 = tk.Button(root, bg="lightblue")
btn_5.bind("<Button-1>", check_color)
btn_5.pack(fill='x')
btn_6 = tk.Button(root, bg='blue')
btn_6.bind("<Button-1>", check_color)
btn_6.pack(fill='x')
btn_7 = tk.Button(root, bg='violet')
btn_7.bind("<Button-1>", check_color)
btn_7.pack(fill='x')

root.mainloop()