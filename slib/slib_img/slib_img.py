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


class ImgFolder():

    def __init__(self, path):

        self.path = path

    def change_format(self, format, new_folder):
        """
        フォルダ中の画像のフォント変換する
        src: 画像フォルダ
        font: 変換後のフォント
        """

        isExists = os.path.exists(new_folder)

        if isExists:
            print('Directory exists')

        else:

            os.mkdir(new_folder)

            files = sorted(glob.glob(self.path + '/*'))

            for i in tqdm(files):

                img = cv2.imread(i)

                new_path = new_folder + '/' + i.split('/')[-1][:-3] + format

                cv2.imwrite(new_path, img)

    def reverse_index(self, new_folder):

        isExists = os.path.exists(new_folder)

        if isExists:

            print('directory exists!')

        else:

            os.mkdir(new_folder)

            files = sorted(glob.glob(self.path + '/*'))

            format = files[0].split('.')[-1]

            length = len(files)

            for i in tqdm(files):

                length -= 1

                file_name = '%03d' % length + '.' + format

                img = cv2.imread(i)

                save_path = new_folder + '/' + file_name

                cv2.imwrite(save_path, img)










if __name__ == '__main__':
    imgs = ImgFolder('/Users/songminglun/Documents/toa/planter/img/dry_new/1')
    imgs.reverse_index('/Users/songminglun/Documents/toa/planter/img/dry_new/3')
    # imgs.change_images_font('jpg', '/Users/songminglun/Documents/toa/planter/img/dry_new')

