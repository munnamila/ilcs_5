# 2021/4/28
# sou meirin

import cv2
import glob
from tqdm import tqdm
import os

def makeVideo(path, size):
    filelist = os.listdir(path)
    filelist2 = [os.path.join(path, i) for i in filelist]
    filelist2 = sorted(filelist2)
    print(filelist2)
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
    makeVideo('lab_Introduction', (1280, 720))