from tkinter import messagebox
import string
import tkinter as tk

def str_date():
    return str(datetime.now()).replace(' ', '_').replace('.', '_').replace(':', '-')

def format_filename(s):
    valid_chars = "-_() %s%s" % (string.ascii_letters, string.digits)
    filename = ''.join(c for c in s if c in valid_chars)
    if filename != '':
        print (filename[:64])
    else:
        messagebox.showerror('Invalid File Name', 'The file name introduced is invalid')
        raise OSError


master = tk.Tk()

master.title('Enter a name for the weights:')
e = tk.Entry(master, width = 64)
e.pack()

e.focus_set()

def callback():
    name = format_filename(e.get())

b = tk.Button(master, text = 'OK', command = callback)
b.pack()

tk.mainloop()
