import os
from tkinter import *
import tkinter as tk
import tkinter.font as tk_font
from tkinter import filedialog as fd
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, ImageGrab  # for Windows environment

# region ========== Global variables & settings ==========
# # initialize tkinter, with creation of Tk root widget
# # (basic window, title bar as defined by OS window manager)
root = Tk()

# # set default font attributes and assign it to global object "font_style"
font_style = tk_font.Font(family="Courier New", size=10)

# # set title
root.title("Process text (developed by Neven Dujmovic)")

# # set geometry (width x height + x_offset + y_offset)
root.geometry("820x400+300+200")

# # in case you want to make form not resizable just uncomment line below
# form.resizable(0, 0)
# # place tkinter window on top of the others
root.attributes('-topmost', True)
root.update()

# # lets make "parent" TAB control by using tkinter.Notebook widget
# # (https://wiki.tcl-lang.org/page/tkinter.Notebook)
# # widget manages a collection of child windows and
# # displays a single one at a time.
tab_parent = ttk.Notebook(root)


# endregion


# region =================== Tab 1 =======================

# # Will will make a few functions. Those are small code routines made
# # for specific purpose and that will be linked with actions (events)
# # triggered by objects (buttons on window dialog in this case)

# # this function is used to open text file and load its content
# # to the text box widget
def open_text_file():
    # # ensure error handling in case text file is NOT selected
    try:
        # # open select file dialog and assign full path to variable name
        name = fd.askopenfilename()
        # # open text file for reading
        f = open(name, "r")
        # # read all lines in the file with method "read"
        # # variable "lines" is a list that will contain all
        # # lines(text) in the file
        lines = f.read()
        txt_main.insert(tk.END, lines)
        # # close the file after reading the lines.
        f.close()
        # # just for the test - print selected file path in console
        print(name)
    except:
        # # for now you can just ignore "PEP 8:
        # # do not use bare 'except' - Too broad exception clause"
        # # in case of error show message with tkinter "messagebox" object
        messagebox.showinfo(message="Text file not selected.")


# # every call of this function will increase font size by 2 in
# # the txt_main object (of tk.Text type)
def increase_text_font():
    # # assign "size" attribute to a variable
    font_size = font_style['size']
    # # set new "size" to global object "font_style"
    font_style.configure(size=font_size + 2)

# # every call of the function will decrease font size by 2 in
# # the txt_main object (of tk.Text type)
def decrease_text_font():
    # # assign "size" attribute to a variable
    font_size = font_style['size']
    # # set new "size" to global object "font_style"
    font_style.configure(size=font_size - 2)


# # new "child" TAB control will be created (tab1) and added
# # to the parent TAB control (tab_parent)
tab1 = ttk.Frame(tab_parent)
tab_parent.add(tab1, text="Text operations")

# # frame will be created to serve as a container for button controls
frame_topTab1 = Frame(tab1)
frame_topTab1.pack(fill=BOTH)

# # the tkinter button widget "btnOpenFile" will be used to trigger
# # function "open_text_file"
btn_openFile = tk.Button(frame_topTab1, text='File Open', bd='5', command=open_text_file)
btn_openFile.pack(side=LEFT, padx=10, pady=5, anchor='ne')

# # the tkinter button widget "btnTextSizeIncrease" will be used to trigger
# # function "increase_text_font"
btn_textSizeIncrease = tk.Button(frame_topTab1, text='+', bd='5', command=increase_text_font)
btn_textSizeIncrease.pack(side=RIGHT, padx=20, pady=5, anchor='ne')

# # the tkinter button widget "btnTextSizeDecrease" will be used to trigger
# # function "decrease_text_font"
btn_textSizeDecrease = tk.Button(frame_topTab1, text='-', bd='5', command=decrease_text_font)
btn_textSizeDecrease.pack(side=RIGHT, padx=0, pady=5, anchor='ne')

# # tkinter text widget "txt_main" is added to "child" TAB control (tab1).
# # This is place where text file will be loaded.
# # Here we can adjust dimension and background color of text widget and
# # assign previously defined global object "font_style".
# # Any change (e.g. font size) in "font_style" will be directly applied
# # to "text_main".
txt_main = tk.Text(tab1, height=20, width=100, bg='#FFE4E1', font=font_style)

# # this will ensure that all controls will be adjusted as we resize
# # window dialog.
txt_main.pack(side=LEFT, fill=BOTH, expand=YES, padx=10, pady=10, anchor='e')

# # vertical scrollbar will be added and associated with text
# # widget "txt_main"
y_scrollbar = Scrollbar(tab1, orient=VERTICAL, command=txt_main.yview)
y_scrollbar.pack(side=RIGHT, fill=Y)
txt_main["yscrollcommand"] = y_scrollbar.set

# endregion


# region =================== Tab 2 =======================

# # this function is used to pass image data from clipboard to dialog window
def get_image():
    try:
        # path to file where image will be temporally stored
        temp_path = "some_image.gif"
        # get image from windows clipboard
        im = ImageGrab.grabclipboard()
        # save image to temp file
        im.save(temp_path)
        # load image from temp file
        load_for_label = ImageTk.PhotoImage(file=temp_path)
        # set image to tkinter label widget
        lbl_image.config(image=load_for_label)
        # save reference to image in memory
        lbl_image.image = load_for_label
        # clear clipboard
        lbl_image.clipboard_clear()
        # delete temp file
        os.remove(temp_path)
    except:
        # # error will occur if clipboard is empty.
        # # Show message with tkinter "messagebox" object.
        messagebox.showinfo(message="Clipboard is Empty.")


# # new "child" TAB control will be created (tab2) and added
# # to the parent TAB control (tab_parent)
tab2 = ttk.Frame(tab_parent)
tab_parent.add(tab2, text="Image operations")

# # frame will be created to serve as a container for button control
frame_topTab2 = Frame(tab2)
frame_topTab2.pack(fill=BOTH)

# # the tkinter button widget "btn_image" will be used
# # to trigger function "get_image"
btn_image = tk.Button(frame_topTab2, text="Paste image", command=get_image)
btn_image.pack(side=RIGHT, padx=20, pady=5, anchor='ne')

# # the tkinter label widget "lbl_image" is used
# # to display image from clipboard
lbl_image = tk.Label(tab2, width=82)
lbl_image.pack(side=LEFT, fill=BOTH, expand=YES, padx=10, pady=10, anchor='e')

# endregion


# # pack() method organizes the widgets in blocks before placing
# # in the parent widget
tab_parent.pack(expand=1, fill='both')

# # method mainloop() is used when your application is ready to run.
# # mainloop() is an infinite loop used to run the application, wait for an event to occur and
# # process the event as long as the window is not closed
root.mainloop()
