import os
import tkinter as tk

import handlers

# Create the Handlers (a handler manager)
h = handlers.Handlers()

# Main window
window = tk.Tk()
window.title("Pixel Inspector")
window.geometry('500x500')
## Register the window object
h.track(window=window)

# Title text
title = tk.Label(window, text='Pixel Inspector', bg='green', fg='yellow',\
             font=('Arial', 24, 'bold'), width=300, height=100)
title.pack()
## Register the title object
h.track(title=title)

# Menubar
menubar = tk.Menu(window)
## File
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label='Open', command=h.open_file)
filemenu.add_separator()
filemenu.add_command(label='Exit', command=window.quit)
## Compile the menus
menubar.add_cascade(label='File', menu=filemenu)
window.config(menu=menubar)

window.mainloop()