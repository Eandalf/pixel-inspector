import os
import tkinter as tk
from tkinter.filedialog import askopenfilename

import inspector

# Handlers
def open_file():
    filename = askopenfilename()
    # Close the title text
    title.pack_forget()
    # Show the image
    show_image(filename)
    return None

def show_image(filename):
    global img, img_show, pi
    # Load the inspector
    ## Preprocess the path
    full_path = filename.split('/')
    path = os.path.join(os.sep, full_path[0], os.sep, *full_path[1:])
    ## Create the inspector
    pi = inspector.PixelInspector(path)
    img_size = pi.getImgSize()
    ## Resize the window
    window.geometry(str(img_size[1]) + 'x' + str(img_size[0]))

    # Display the image
    img = tk.PhotoImage(file=filename)
    img_show = tk.Label(window, image=img)
    img_show.pack()
    return None

# Main window
window = tk.Tk()
window.title("Pixel Inspector")
window.geometry('500x500')

# Title text
title = tk.Label(window, text='Pixel Inspector', bg='green', fg='yellow',\
             font=('Arial', 24, 'bold'), width=300, height=100)
title.pack()

# Menubar
menubar = tk.Menu(window)
## File
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label='Open', command=open_file)
filemenu.add_separator()
filemenu.add_command(label='Exit', command=window.quit)
## Compile the menus
menubar.add_cascade(label='File', menu=filemenu)
window.config(menu=menubar)

#show_image('./demo/stinkbug.png')

window.mainloop()