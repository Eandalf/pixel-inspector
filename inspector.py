import os

import numpy as np
import matplotlib.image as mpimg

def inspector(path, x, y):
    img = mpimg.imread(path)
    pixel = 255 * img[x, y, :]

    return pixel.astype(int)

path = os.path.join('./demo', 'stinkbug.png')
# dir_path = '' # A linux style absolute path.
# dir_path = dir_path.split('/')
# path = os.path.join(os.sep, dir_path[0], os.sep, *dir_path[1:], 'stinkbug.png')
# print(path)

try:
    print(inspector(path, 300, 300))
except IndexError:
    print("Index is out of bound. Please check the image size.")