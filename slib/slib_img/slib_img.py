# sou meirin
import cv2
import numpy as np
import matplotlib.pyplot as plt

import slib_os  as so

class Img():

    def __init__(self, path):
        '''import picture'''

        self.path = path
        self.img = cv2.imread(self.path)
        print(self.img.shape)

    def shape(self):
        # I.size()

        return self.img.shape

    def to_gray(self):
        '''グレー化'''

        self.img = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)

        return self.img


    def to_RGB(self):

        self.img = cv2.cvtColor(self.img, cv2.COLOR_BGR2RGB)

        return self.img

    def to_BGR(self):

        self.img = cv2.cvtColor(self.img, cv2.COLOR_RGB2BGR)

        return self.img

    def ori(self):

        self.img = self.img

        return self.img


    def show(self):

        if self.img.ndim == 3:
            plt.imshow(self.img)
        elif self.img.ndim == 2:
            plt.imshow(self.img, cmap='gray')
        plt.show()

    def save(self):

        print(self.path.split('.'))

        # cv2.imwrite(self.path, self.img) 

    def resize(self, height, weight):

        self.img = cv2.resize(self.img, (height, weight))

if __name__ == '__main__':
    pass

