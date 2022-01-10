import numpy as np
import glob
import matplotlib.pyplot as plt
from tqdm import tqdm
import cv2

def __version__():
    print('1.0.0')

def keypoints_plot(src, src_img = None, plot_in_pic = False, show_accuracy = False):
    
    list_x, list_y, list_accuracy = [], [], []
        
    if plot_in_pic == False:
        
        for i in src[0]:
            list_x.append(i[0])
            list_y.append(-i[1])
            list_accuracy.append(i[2])
        
        plt.figure(figsize = (16, 9))
        plt.scatter(list_x, list_y)
        plt.show()
        
    elif plot_in_pic == True:
        
        for i in src[0]:
            list_x.append(i[0])
            list_y.append(i[1])
            list_accuracy.append(i[2])

                
        plt.figure(figsize = (16, 9))
        img = cv2.imread(src_img)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        plt.imshow(img)
        plt.scatter(list_x, list_y)
        plt.show()


    
if __name__ == '__main__':
    pass