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
# from PIL import ImageTk, ImageGrab  # for Windows environment
import pyscreenshot as ImageGrab  # for Linux environment
from PIL import ImageTk  # for Linux environment

# region Global variables
root = Tk()
font_style = tk_font.Font(family="Courier New", size=10)
root.title("Process text (developed by Neven Dujmovic)")
root.geometry("820x400+300+200")
# make form not resizable
# form.resizable(0, 0)
tab_parent = ttk.Notebook(root)


# endregion


# region Tab 1
def open_text_file():
    name = fd.askopenfilename()
    f = open(name, "r")
    # use readlines to read all lines in the file
    # The variable "lines" is a list containing all lines in the file
    lines = f.readlines()
    txtMain.insert(tk.END, lines)
    # close the file after reading the lines.
    f.close()
    print(name)


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

txtMain = tk.Text(tab1, height=20, width=100, bg='#FFE4E1', font=font_style)
txtMain.pack(side=LEFT, fill=BOTH, expand=YES, padx=10, pady=10, anchor='e')
y_scrollbar = Scrollbar(tab1, orient=VERTICAL, command=txtMain.yview)
y_scrollbar.pack(side=RIGHT, fill=Y)
txtMain["yscrollcommand"] = y_scrollbar.set


# endregion


# region Tab 2
def get_image():
    try:
        temp_path = "some_image.gif"  # Whatever temp path you want here
        # im = ImageGrab.grabclipboard()  # Get image from clipboard Windows
        im = ImageGrab.grab()  # Get image from clipboard Linux

        im.save(temp_path)  # save image to temp folder
        load_for_label = ImageTk.PhotoImage(file=temp_path)  # load image from temp folder
        lblImage.config(image=load_for_label)  # set image to label
        lblImage.image = load_for_label  # save reference to image in memory

        lblImage.clipboard_clear()  # clear clipboard
        os.remove(temp_path)  # delete temp file
        print(temp_path)
    except (ValueError, Exception):
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


# place tkinter window on top of the others
root.attributes('-topmost', True)
root.update()

tab3 = ttk.Frame(tab_parent)
tab_parent.add(tab3, text="Web operations")

# back to normal tkinter window
# form.attributes('-topmost', False)

tab_parent.pack(expand=1, fill='both')

root.mainloop()
