from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
import os
from datetime import datetime

root = Tk()
root.title("Sorter")
root.geometry("500x150+400+200")

style = ttk.Style()
style.configure("my.TButton", font=("Helvetica", 15))

def choice_dir():
    file_dir = filedialog.askdirectory()
    e_path.delete(0, "end")
    e_path.insert(0, file_dir)

def s_start():
    cur_path = e_path.get()
    if cur_path:
        for folder, subfolder, files in os.walk(cur_path):
            for file in files:
                path = os.path.join(folder, file)
                mtime = os.path.getmtime(path)
                date = datetime.fromtimestamp(mtime)
                date = date.strftime("%Y-%m-%d")
                date_folder = os.path.join(cur_path, date)
                if not os.path.exists(date_folder):
                    os.mkdir(date_folder)
                os.rename(path, os.path.join(date_folder, file))
        messagebox.showinfo("Success", "Well done!")
        e_path.delete(0, "end")
    else:
        messagebox.showwarning("Warning", "Chose folder with files")



frame = Frame(root, bg="green", bd=5)
frame.pack(pady=10, padx=10, fill="x")

e_path = ttk.Entry(frame)
e_path.pack(side=LEFT, ipady=2, expand=True, fill="x")

btn_dialog = ttk.Button(frame, text="Выбрать папкку: ", command=choice_dir)
btn_dialog.pack(side=LEFT, padx=5)

btn_start = ttk.Button(root, style="my.TButton", text="Начать сортировку ", command=s_start)
btn_start.pack(fill="x", padx=5)

root.mainloop()
