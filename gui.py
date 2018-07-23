import os
import tkinter as tk
from threading import Thread
from scripts.smartscope import main as smartscope_micro
from scripts.importweights import main as import_weights

def create_weights():
    new_thread(os.system, 'python scripts/createweights.py')

def instatrain():
    new_thread(os.system, 'python scripts/instatrainwrapper.py')

def new_thread(func, arg = None):
    t = Thread(target = func, args = (arg,) if arg else ())
    t.start()
    t.join()

def dialog():
    # tkinter set up
    master = tk.Tk()
    master.resizable(False, False)
    master.title('SmartScope')

    # create buttons
    launch_sprite = tk.PhotoImage(file='sprites/launch.png')
    launch_button = tk.Button(master, image = launch_sprite, command = None)
    import_sprite = tk.PhotoImage(file='sprites/import.png')
    import_button = tk.Button(master, image = import_sprite, command = import_weights)
    create_sprite = tk.PhotoImage(file='sprites/create.png')
    create_button = tk.Button(master, image = create_sprite, command = create_weights)
    instatrain_sprite = tk.PhotoImage(file='sprites/instatrain.png')
    instatrain_button = tk.Button(master, image = instatrain_sprite, command = instatrain)

    launch_button.pack()
    import_button.pack()
    create_button.pack()
    instatrain_button.pack()

    tk.mainloop()

new_thread(dialog)
