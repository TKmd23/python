import tkinter as tk

root = tk.Tk()
root.geometry("1000x500+250+100")

def adder():
    enter.insert("end", "TKmd")

def deller():
    enter.delete(0, "end")

def getter():
    label2['text'] = enter.get()



label = tk.Label(root, text="Entery box")
label.pack()

label2 = tk.Label(root, text="paster", bg="green")
label2.pack(fill='x')

enter = tk.Entry(root, show="*")
# enter.insert(0, "Hello")
# enter.insert("end", " world!")
# enter.delete(6, "end")
enter.pack()

btn_add = tk.Button(root, text="Add", command=adder)
btn_add.pack()
btn_del = tk.Button(root, text="Del", command=deller)
btn_del.pack()
btn_get = tk.Button(root, text="Get", command=getter)
btn_get.pack()



root.mainloop()