import string
import tkinter as tk
from tkinter import messagebox
from instatrain import instatrain

# lists to store entry objects and inputted classes
entries = []
classes = []

# make string filename friendly
def format_filename(s):
    valid_chars = '-_()' + string.ascii_letters + string.digits
    filename = ''.join(c for c in s if c in valid_chars)
    if filename != '':
        return filename[:64]
    else:
        messagebox.showerror('Invalid Weights Name', 'The weight name introduced is invalid')
        exit()

# append entry
def add_entry():
    global entries
    aux = tk.Entry(master, width = 40)
    entries.append(aux)
    aux.pack()

# remove last entry
def delete_entry():
    global entries
    if len(entries) >= 2:
        entries[-1].destroy()
        entries = entries[:-1]

# add text to dialog
def add_label(string):
    labelText = tk.StringVar()
    labelText.set(string)
    labelDir = tk.Label(master, textvariable = labelText)
    labelDir.pack()

# get name and classes, begin instatrain
def ok_action():
    name = format_filename(name_entry.get())
    for entry in entries:
        if entry.get():
            classes.append(entry.get().replace('"', ''))
    master.destroy()
    if len(classes) >= 2:
        instatrain(name, tuple(classes))
    else:
        root = tk.Tk()
        root.withdraw()
        messagebox.showerror('Not Enough Clases', 'Not enough classes introduced')

# tkinter set up
master = tk.Tk()
master.resizable(False, False)
master.title('Instatrain')

add_label('Enter name of weights')

# add entry for weights name
name_entry = tk.Entry(master, width = 40)
name_entry.pack()
name_entry.focus_set()

add_label('Enter classes')

# append add annother classbutton
add_entry_button = tk.Button(master, text = 'Add another class', command = add_entry)
add_entry_button.pack()

for i in range(2):
    add_entry()

# append OK button
ok = tk.Button(master, text = 'OK', command = ok_action)
ok.pack(side = tk.BOTTOM)

# append delete last entry button
remove_entry_button = tk.Button(master, text = 'Delete entry', command = delete_entry)
remove_entry_button.pack(side = tk.BOTTOM)

master.mainloop()
