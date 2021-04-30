# 2021/4/30
# sou meirin
# python path w h
# python /Users/songminglun/Documents/ILCS/code/0_ConpisiteVideo/videomurasei 854 480

import cv2
import glob
from tqdm import tqdm
import os
import argparse

def makeVideo(path, size):
    filelist = os.listdir(path)
    filelist2 = [os.path.join(path, i) for i in filelist]
    filelist2 = sorted(filelist2)
    # print(filelist2)
    fps = 30  
    video = cv2.VideoWriter(path + "/Video.mp4", cv2.VideoWriter_fourcc('M', 'P', '4', 'v'), fps,
                            size) 

    for item in tqdm(filelist2):
        # print(item)
        if item.endswith('.jpg'):
            # print(item)
            img = cv2.imread(item)
            video.write(img)

    video.release()
    cv2.destroyAllWindows()
    print('DONE')

        

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='input images dirctory, img_size')
    parser.add_argument('path', type = str, help = 'inputed path and size')
    parser.add_argument('w', type = int, help = 'w')
    parser.add_argument('h', type = int, help = 'h')
    args = parser.parse_args()

    makeVideo(args.path, (args.w, args.h))
    # makeVideo(args.path, (854, 480))