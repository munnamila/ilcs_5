# 2021/4/30
# sou meirin
# python path w h
# python /Users/songminglun/Documents/ILCS/code/0_ConpisiteVideo/videomurasei 854 480

import cv2
import glob
# from tqdm import tqdm
import os
import argparse

def frame2video(path):

    path_img = sorted(glob.glob(path + '/*'))[0]
    img = cv2.imread(path_img)
    size_img = img.shape
    w = size_img[1]
    h = size_img[0]

    size = (w, h)

    filelist = os.listdir(path)
    filelist2 = [os.path.join(path, i) for i in filelist]
    filelist2 = sorted(filelist2)
    # print(filelist2)
    fps = 30  
    video = cv2.VideoWriter(path + "/Video.avi", cv2.VideoWriter_fourcc('M','J','P','G'), fps,
                            size) 

    for item in filelist2:
        # print(item)
        if item.endswith('.jpg'):
            # print(item)
            img = cv2.imread(item)
            video.write(img)

    video.release()
    cv2.destroyAllWindows()
    print('DONE')

        

if __name__ == '__main__':
    pass
    # parser = argparse.ArgumentParser(description='input images dirctory, img_size')
    # parser.add_argument('path', type = str, help = 'inputed path and size')
    # parser.add_argument('w', type = int, help = 'w')
    # parser.add_argument('h', type = int, help = 'h')
    # args = parser.parse_args()

    # frame2video(args.path, (args.w, args.h))
    # makeVideo(args.path, (854, 480))