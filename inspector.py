import os

import numpy as np
import matplotlib.image as mpimg

class PixelInspector:
    def __init__(self, path):
        try:
            self.img = mpimg.imread(path)
        except FileNotFoundError:
            print("No such file or directory.")
            self.img = np.zeros((100,100,3))
    
    def inspect(self, x,y):
        try:
            pixel = 255 * self.img[x, y, :]
        except IndexError:
            print("Index is out of bound. Please check the image size.")
        
        return pixel.astype(int)
    
    def getImgSize(self):
        return self.img.shape[:2]
    
    @staticmethod
    def demo():
        path = os.path.join('./demo', 'stinkbug.png')
        pi = PixelInspector(path)
        print(pi.inspect(300, 300))
