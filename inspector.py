import os

import numpy as np
import matplotlib.image as mpimg

class PixelInspector:
    # path: A linux style absolute path.
    def __init__(self, path):
        try:
            # Preprocess the path
            path_converted = path.split('/')
            if path_converted[-1].split('.')[-1] != 'png':
                raise NotImplementedError('Only png files are supported.')

            if path_converted[0] != '.' and path_converted[0] != '..':
                path_converted = os.path.join(os.sep, path_converted[0],\
                                             os.sep, *path_converted[1:])
            else:
                path_converted = os.path.join(*path_converted)
            
            self.img = mpimg.imread(path_converted)
        except FileNotFoundError:
            print("No such file or directory.")
            self.img = np.zeros((100,100,3))
    
    def inspect(self, x, y):
        try:
            pixel = 255 * self.img[y, x, :]
        except IndexError:
            print("Index is out of bound. Please check the image size.")
        
        return pixel.astype(int)
    
    def getImgSize(self):
        return self.img.shape[:2]
    
    @staticmethod
    def demo():
        path = './demo/stinkbug.png'
        pi = PixelInspector(path)
        print(pi.inspect(300, 300))

if __name__ == '__main__':
    PixelInspector.demo()
