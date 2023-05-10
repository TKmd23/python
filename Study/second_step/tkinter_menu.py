import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

root = tk.Tk()
root.geometry("600x400+300+100")


def about_programm():
    messagebox.showinfo(title='Error', message="Fuck off")


def my_exit():
    if messagebox.askokcancel(title="Exit", message="Do you want to exit"):
        root.destroy()


def open_file():
    file_pass = filedialog.askopenfilename(title="Open file", filetypes=(("Text documents", "*.txt"),
                                                                         ("All types", "*.*")))
    if file_pass:
        text.delete("1.0", "end")
        file = open(file_pass, encoding='utf-8')
        text.insert("1.0", file.read())
        file.close()

def save_file():
    new_file_pass = filedialog.asksaveasfilename(title="Save as", filetypes=(("Text documents", "*.txt"),
                                                                             ("All types", "*.*")))
    file = open(new_file_pass+'.txt', encoding='utf-8', mode='w')
    data = text.get('1.0', 'end')
    file.write(data)
    file.close()

def theme_color(color):
    text['bg'] = colors[color]['bg']
    text['fg'] = colors[color]['fg']
    text['insertbackground'] = colors[color]['insertbackground']
    text['selectbackground'] = colors[color]['selectbackground']


main_menu = tk.Menu(root)
root.config(menu=main_menu)

file_menu = tk.Menu(main_menu, tearoff=0)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=my_exit)
main_menu.add_cascade(label="File", menu=file_menu)

about_menu = tk.Menu(main_menu, tearoff=0)
help_menu = tk.Menu(about_menu, tearoff=0)
about_menu.add_command(label="TKmd")
about_menu.add_command(label="Updates", command=about_programm)
help_menu.add_command(label="Light", command=lambda: theme_color('light'))
help_menu.add_command(label="Dark", command=lambda: theme_color('dark'))
main_menu.add_cascade(label="About", menu=about_menu)
about_menu.add_cascade(label="Themes", menu=help_menu)

frame_text = tk.Frame(root)
frame_text.pack(fill="both", expand=True)

colors = {
    "dark": {
        "bg": "#343D46",
        "fg": '#C6DEC1',
        "insertbackground": "#eda756",
        "selectbackground": "#4e5a65"
    },
    "light": {
        "bg": "#fff",
        "fg": '#000',
        "insertbackground": "#8000ff",
        "selectbackground": "#777"
    }
}

text = tk.Text(frame_text, bg=colors['dark']['bg'], fg=colors['dark']['fg'], padx=10, pady=10, wrap='word',
               insertbackground=colors['dark']['insertbackground'], selectbackground=colors['dark']['selectbackground'],
               spacing3=10, width=30)
text.pack(fill="both", expand=True, side='left')

scroll = tk.Scrollbar(frame_text, command=text.yview, bg='#1F252A')
scroll.pack(fill='y', side='right')
text.configure(yscrollcommand=scroll.set)

root.mainloop()
