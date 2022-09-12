# sou meirin
import cv2
import numpy as np
import matplotlib.pyplot as plt
import glob
from tqdm import tqdm
import os

import slib_os  as so

def test():
    print('Okay')

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

        cv2.imwrite(self.path, self.img) 

    def resize(self, height, weight):

        self.img = cv2.resize(self.img, (height, weight))

def change_images_font(src, font, size=None):
    """
    フォルダ中の画像のフォント変換する
    src: 画像フォルダ
    font: 変換後のフォント
    """

    files = sorted(glob.glob(src + '/*'))

    for i in tqdm(files):

        img = cv2.imread(i)

        if size != None:

            img = cv2.resize(img, size)

        new_path = i[:-3] + font

        os.system('rm ' + str(i))

        cv2.imwrite(new_path, img)





if __name__ == '__main__':
    change_font_of_images('/Users/songminglun/Documents/toa/planter/220613＿png改jpg/sq1', 'jpg')

