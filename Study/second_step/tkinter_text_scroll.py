import tkinter as tk


root = tk.Tk()
root.geometry("600x400+300+100")

frame_menu = tk.Frame(root, bg='#1F252A', height=40)
frame_text = tk.Frame(root)
frame_menu.pack(fill='x')
frame_text.pack(fill="both", expand=True)

l_menu = tk.Label(frame_menu, text="Menu", bg="#2B3239", fg="#C6DEC1", font="Arial 10")
l_menu.place(x=10, y=10)

def add_str():
    text.insert('end', "hello!")

def del_str():
    text.delete('1.0', 'end')


def get_str():
    print(text.get('1.0', 'end'))

btn_add = tk.Button(frame_menu, text="Add", command=add_str).place(x=50, y=10)
btn_del = tk.Button(frame_menu, text="Delete", command=del_str).place(x=90, y=10)
btn_get = tk.Button(frame_menu, text="Get", command=get_str).place(x=140, y=10)

text = tk.Text(frame_text, bg="#343D46", fg='#C6DEC1', padx=10, pady=10, wrap='word', insertbackground="#eda756",
               selectbackground="#4e5a65", spacing3=10, width=30)
text.pack(fill="both", expand=True, side='left')

scroll = tk.Scrollbar(frame_text, command=text.yview, bg='#1F252A')
scroll.pack(fill='y', side='right')
text.configure(yscrollcommand=scroll.set)

root.mainloop()

'''Lorem ipsum dolor sit amet, consectetur adipiscing elit,
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
Ut enim ad minim veniam, quis nostrud exercitation ullamco
laboris nisi ut aliquip ex ea commodo consequat.
Duis aute irure dolor in reprehenderit in voluptate velit esse 
cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat
cupidatat non proident, sunt in culpa qui officia deserunt
mollit anim id est laborum.'''