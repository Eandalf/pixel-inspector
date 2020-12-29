import tkinter as tk
from tkinter.filedialog import askopenfilename
import tkinter.messagebox as msbox

import inspector

class Handlers:
    def __init__(self):
        self.ui_obj = {}
        return None
    
    # Track the UI objects
    def track(self, **kwargs):
        for key, value in kwargs.items():
            self.ui_obj[key] = value
    
    # Track the cursor position
    def motion(self, event):
        self.x, self.y = event.x, event.y
        # print('{}, {}'.format(self.x, self.y))

        # Size checking
        if hasattr(self, 'img_width') and hasattr(self, 'img_height'):
            if self.x >= self.img_width or self.y >= self.img_height:
                return None

        # Update the position values
        if 'position' in self.ui_obj:
            self.ui_obj['position'].config(text='(' + str(self.x) +\
                                         ', ' + str(self.y) + ')')
        
        # Update the pixel displaying values
        if 'value' in self.ui_obj:
            pixel = self.pi.inspect(self.x, self.y)
            if len(pixel) == 3:
                self.ui_obj['value_type'].config(text='RGB')
                self.ui_obj['value'].config(text='(' + str(pixel[0]) +\
                                             ', ' + str(pixel[1]) +\
                                             ', ' + str(pixel[2]) +  ')')
            elif len(pixel) == 4:
                self.ui_obj['value_type'].config(text='RGBA')
                self.ui_obj['value'].config(text='(' + str(pixel[0]) +\
                                             ', ' + str(pixel[1]) +\
                                             ', ' + str(pixel[2]) +\
                                             ', ' + str(pixel[3]) +  ')')

        return None

    def open_file(self):
        filename = askopenfilename()
        # Close the title text
        self.ui_obj['title'].pack_forget()
        try:
            # Show the image
            self.show_image(filename)
        except NotImplementedError as e:
            msbox.showerror(title='Error', message=e.args[0])
        return None

    def show_image(self, filename):
        # Load the inspector
        self.pi = inspector.PixelInspector(filename)
        img_size = self.pi.getImgSize()
        self.img_width = img_size[0]
        self.img_height = img_size[1]
        # Resize the window
        self.ui_obj['window'].geometry(str(self.img_width) + 'x'\
                                         + str(self.img_height + 50))

        # Clear the old image if it exists
        if 'img_show' in self.ui_obj:
            self.ui_obj['img_show'].destroy()

        # Display the image
        self.ui_obj['img'] = tk.PhotoImage(file=filename)
        self.ui_obj['img_show'] = tk.Label(self.ui_obj['window'],\
                                             image=self.ui_obj['img'])
        self.ui_obj['img_show'].pack()

        # Clear the old text area if it exists
        if 'text_area' in self.ui_obj:
            self.ui_obj['position_title'].destroy()
            self.ui_obj['position'].destroy()
            self.ui_obj['value_type'].destroy()
            self.ui_obj['value'].destroy()
            self.ui_obj['text_area'].destroy()

        # Create the text area
        self.ui_obj['text_area'] = tk.Frame(self.ui_obj['window'])
        self.ui_obj['text_area'].pack()

        self.ui_obj['position_title'] = tk.Label(self.ui_obj['text_area'],\
                                             text='Position',\
                                             font=('Arial', 14, 'bold'))
        self.ui_obj['position_title'].grid(row=0, column=0)

        self.ui_obj['position'] = tk.Label(self.ui_obj['text_area'],\
                                             text='(0, 0)',\
                                             font=('Arial', 14, 'bold'))
        self.ui_obj['position'].grid(row=0, column=1, padx=(0,25))

        self.ui_obj['value_type'] = tk.Label(self.ui_obj['text_area'],\
                                             text='RGB',\
                                             font=('Arial', 14, 'bold'))
        self.ui_obj['value_type'].grid(row=0, column=2, padx=(25, 0))
        
        self.ui_obj['value'] = tk.Label(self.ui_obj['text_area'],\
                                         text='(0, 0, 0)',\
                                         font=('Arial', 14, 'bold'))
        self.ui_obj['value'].grid(row=0, column=3)
        return None