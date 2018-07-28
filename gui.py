import os, webbrowser, shutil
import tkinter as tk
from threading import Thread
from scripts.smartscope import main as smartscope_micro_func
from scripts.importweights import main as import_weights

# launch routine on a new thread
def new_thread(func, arg = None):
    t = Thread(target = func, args = (arg,) if arg else ())
    t.start()
    t.join()

# buttons callbacks
def create_weights():
    new_thread(os.system, 'python3 scripts/createweights.py')

def instatrain():
    new_thread(os.system, 'python3 scripts/instatrainwrapper.py')

def smartscope_micro():
    global master
    master.destroy()
    smartscope_micro_func()

def macro():
    macro_file = 'tf_files/macro.txt'
    if not os.path.isfile(macro_file):
        shutil.copyfile('tf_files/default_macro.txt', macro_file)
    webbrowser.open(macro_file)

def dialog():
    # tkinter set up
    global master
    master = tk.Tk()
    master.resizable(False, False)
    master.title('SmartScope')

    # create buttons
    launch_sprite = tk.PhotoImage(file = 'sprites/launch.png')
    launch_button = tk.Button(master, image = launch_sprite, command = smartscope_micro)
    import_sprite = tk.PhotoImage(file = 'sprites/import.png')
    import_button = tk.Button(master, image = import_sprite, command = import_weights)
    create_sprite = tk.PhotoImage(file = 'sprites/create.png')
    create_button = tk.Button(master, image = create_sprite, command = create_weights)
    instatrain_sprite = tk.PhotoImage(file = 'sprites/instatrain.png')
    instatrain_button = tk.Button(master, image = instatrain_sprite, command = instatrain)
    macro_sprite = tk.PhotoImage(file = 'sprites/blank.png')
    macro_button = tk.Button(master, image = macro_sprite, command = macro)

    launch_button.pack()
    import_button.pack()
    create_button.pack()
    instatrain_button.pack()
    macro_button.pack()

    tk.mainloop()

# main
new_thread(dialog)
