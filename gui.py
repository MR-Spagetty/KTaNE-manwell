##
# gui.py
# file that contains the gui for the manual

# MR-Spagetty

import tkinter as tk
from PIL import Image, ImageTk


def load_module():
    pass

path = __file__.replace('gui.py', '')
modules = ['wires', 'whos on first']
print(path)


def menu_setup(modules):
    menu = tk.Tk()
    menu.title('MENU')

    module_drop = tk.Menubutton(menu, text='Select module')
    module_drop_menu = tk.Menu(module_drop)
    module_drop['menu'] = module_drop_menu
    selected_module = tk.StringVar()
    for module in modules:
        module_drop_menu.add_radiobutton(variable=selected_module, value=module, label=module)
    module_drop.pack()
    menu.mainloop()

menu_setup(modules)
