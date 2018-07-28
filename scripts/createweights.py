import shutil, os, string
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

# removes invalid  characters from file name
def format_filename(s):
    valid_chars = "-_() %s%s" % (string.ascii_letters, string.digits)
    filename = ''.join(c for c in s if c in valid_chars)
    if filename != '':
        return filename[:64]
    else:
        messagebox.showerror('Invalid File Name', 'The file name introduced is invalid')
        exit()

# weights name dialog
master = tk.Tk()
master.resizable(False, False)
master.title('Enter a name for the weights:')

# entry field
e = tk.Entry(master, width = 50)
e.pack(side = tk.LEFT)
e.focus_set()

def callback():
    global name
    name = format_filename(e.get())
    master.destroy()

# ok button
b = tk.Button(master, text = 'OK', command = callback)
b.pack(side = tk.LEFT)

tk.mainloop()

# checks if the dialog was closed
try:
    name
except NameError:
    master = tk.Tk()
    master.withdraw()
    messagebox.showerror('Name Error', 'No name introduced')
    exit()

# choose directory dialog
master = tk.Tk()
master.withdraw()
file_path = filedialog.askdirectory()

# check if a directory was chosen
if file_path == '':
    messagebox.showerror('Directory Error', 'No directory selected')
    exit()

# train the neural network
os.system('python3 scripts/retrain.py --bottleneck_dir=tf_files/bottlenecks  --image_dir='
          + file_path + '  --output_graph=tf_files/' + name + '.pb --output_labels=tf_files/'
          + name + '.txt')
