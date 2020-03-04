# #####################################################################################################################
# ######################### by Neven Dujmovic Feb 2020 - Utility desktop tool - tkinter Python ########################
# #####################################################################################################################

import os
from tkinter import *
import tkinter as tk
import tkinter.font as tk_font
from tkinter import filedialog as fd
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, ImageGrab  # for Windows environment

# import pyscreenshot as ImageGrab  # for Linux environment
# from PIL import ImageTk  # for Linux environment


# region ========== Global variables & settings ==========

# initialize tkinter, with creation of Tk root widget (basic window, title bar as defined by OS window manager)
root = Tk()

# add default font, title and geometry
font_style = tk_font.Font(family="Courier New", size=10)
root.title("Process text (developed by Neven Dujmovic)")
# (width x height + x_offset + y_offset)
root.geometry("820x400+300+200")

# in case you want to make form not resizable just uncomment line below
# form.resizable(0, 0)

# place tkinter window on top of the others
root.attributes('-topmost', True)
root.update()

# lets make TAB control by using tkinter.Notebook widget (https://wiki.tcl-lang.org/page/tkinter.Notebook)
# widget manages a collection of child windows and displays a single one at a time..
tab_parent = ttk.Notebook(root)

# endregion


# region =================== Tab 1 =======================

# this function is used to open text file and load its content to text box widget
def open_text_file():
    # ensure error handling in case text file is NOT selected
    try:
        # open select file dialog and assign full path to variable name
        name = fd.askopenfilename()

        # open text file for reading
        f = open(name, "r")

        # all lines in the file with readlines
        # The variable "lines" is a list containing all lines in the file
        lines = f.readlines()
        txt_main.insert(tk.END, lines)

        # close the file after reading the lines.
        f.close()
        # just for the test - print selected file path in console
        print(name)
    except:
        messagebox.showinfo(message="Text file not selected.")


def increase_text_font():
    font_size = font_style['size']
    font_style.configure(size=font_size + 2)


def decrease_text_font():
    font_size = font_style['size']
    font_style.configure(size=font_size - 2)


def process_text():
    pass


tab1 = ttk.Frame(tab_parent)
tab_parent.add(tab1, text="Text operations")

frameTopTab1 = Frame(tab1)
frameTopTab1.pack(fill=BOTH)

btnOpenFile = tk.Button(frameTopTab1, text='File Open', bd='5', command=open_text_file)
btnOpenFile.pack(side=LEFT, padx=10, pady=5, anchor='ne')

btnTextSizeIncrease = tk.Button(frameTopTab1, text='+', bd='5', command=increase_text_font)
btnTextSizeIncrease.pack(side=RIGHT, padx=20, pady=5, anchor='ne')

btnTextSizeDecrease = tk.Button(frameTopTab1, text='-', bd='5', command=decrease_text_font)
btnTextSizeDecrease.pack(side=RIGHT, padx=0, pady=5, anchor='ne')

txt_main = tk.Text(tab1, height=20, width=100, bg='#FFE4E1', font=font_style)
txt_main.pack(side=LEFT, fill=BOTH, expand=YES, padx=10, pady=10, anchor='e')
y_scrollbar = Scrollbar(tab1, orient=VERTICAL, command=txt_main.yview)
y_scrollbar.pack(side=RIGHT, fill=Y)
txt_main["yscrollcommand"] = y_scrollbar.set


# endregion


# region =================== Tab 2 =======================
def get_image():
    try:
        temp_path = "some_image.gif"  # Whatever temp path you want here
        im = ImageGrab.grabclipboard()  # Get image from clipboard Windows
        # im = ImageGrab.grab()  # Get image from clipboard Linux

        im.save(temp_path)  # save image to temp folder
        load_for_label = ImageTk.PhotoImage(file=temp_path)  # load image from temp folder
        lblImage.config(image=load_for_label)  # set image to label
        lblImage.image = load_for_label  # save reference to image in memory

        lblImage.clipboard_clear()  # clear clipboard
        os.remove(temp_path)  # delete temp file
        print(temp_path)
    except:
        messagebox.showinfo(message="Clipboard is Empty.")


tab2 = ttk.Frame(tab_parent)
tab_parent.add(tab2, text="Image operations")

frameTopTab2 = Frame(tab2)
frameTopTab2.pack(fill=BOTH)

btnImage = tk.Button(frameTopTab2, text="IMAGE", command=get_image)
btnImage.pack(side=RIGHT, padx=20, pady=5, anchor='ne')

lblImage = tk.Label(tab2, width=82)
lblImage.pack(side=LEFT, fill=BOTH, expand=YES, padx=10, pady=10, anchor='e')
# endregion


tab3 = ttk.Frame(tab_parent)
tab_parent.add(tab3, text="Web operations")

# back to normal tkinter window
# form.attributes('-topmost', False)

tab_parent.pack(expand=1, fill='both')

root.mainloop()
