import os
import tkinter as tk

import inspector

dir_path = '' # A linux style absolute path.
dir_path = dir_path.split('/')
path = os.path.join(os.sep, dir_path[0], os.sep, *dir_path[1:], 'stinkbug.png')
print(path)

pi = inspector.PixelInspector(path)
img_size = pi.getImgSize()
print(img_size)

window = tk.Tk()
window.title("Pixel Inspector")
window.geometry(str(img_size[1]) + 'x' + str(img_size[0]))
window.mainloop()