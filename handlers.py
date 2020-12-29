import tkinter as tk
from tkinter.filedialog import askopenfilename

import inspector

class Handlers:
    def __init__(self):
        self.ui_obj = {}
        return None
    
    # Track the UI objects
    def track(self, **kwargs):
        for key, value in kwargs.items():
            self.ui_obj[key] = value

    def open_file(self):
        filename = askopenfilename()
        # Close the title text
        self.ui_obj['title'].pack_forget()
        # Show the image
        self.show_image(filename)
        return None

    def show_image(self, filename):
        # Load the inspector
        self.pi = inspector.PixelInspector(filename)
        img_size = self.pi.getImgSize()
        # Resize the window
        self.ui_obj['window'].geometry(str(img_size[1]) + 'x'\
                                         + str(img_size[0]))

        # Clear the old image if it exists
        if 'img_show' in self.ui_obj:
            self.ui_obj['img_show'].destroy()

        # Display the image
        self.ui_obj['img'] = tk.PhotoImage(file=filename)
        self.ui_obj['img_show'] = tk.Label(self.ui_obj['window'],\
                                             image=self.ui_obj['img'])
        self.ui_obj['img_show'].pack()
        return None