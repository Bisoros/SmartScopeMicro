import os, shutil
import tkinter as tk
from tkinter import filedialog
from shutil import copyfile
from tkinter import messagebox
from os.path import abspath

# routine that checks if labels file exists
def check_file(filename):
    return os.path.isfile(filename.replace('.pb', '.txt'))

def main():
    # tkinter set up
    root = tk.Tk()
    root.withdraw()

    # import weights diologs
    file_path = filedialog.askopenfilename(title = 'Import Weights',
                filetypes = (('protocol buffers','*.pb'),('all files','*.*')))

    if file_path == '':
        messagebox.showerror('Selection Error', 'No file selected')
        return

    if (check_file(file_path)):
        shutil.copy2(file_path, abspath('tf_files'))
        shutil.copy2(file_path.replace('.pb', '.txt'), abspath('tf_files'))
    else:
        messagebox.showerror('Import Error', 'No labels file')

if __name__ == '__main__':
    main()
