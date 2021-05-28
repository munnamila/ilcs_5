from os import name
from platform import machine
import cv2
import glob
import time
import os

def imshow(src):

    files = sorted(glob.glob(src + '/*'))
    for i in files:
        img = cv2.imread(i)
        cv2.imshow('test', img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# def frame2video(path, size, mode = 0):
#     filelist = os.listdir(path)
#     filelist2 = [os.path.join(path, i) for i in filelist]
#     filelist2 = sorted(filelist2)
#     # print(filelist2)
#     fps = 30  

#     out = time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime())

#     if mode == 1:
#         video = cv2.VideoWriter(path + "/Video.avi", cv2.VideoWriter_fourcc('M','J','P','G'), fps,
#                             size) 

#     elif mode == 0:
#         video = cv2.VideoWriter('/Users/songminglun/Documents/ILCS/ilcs_5/slib/slib_img/saved_video/' + str(out) + '.avi', cv2.VideoWriter_fourcc('M','J','P','G'), fps,
#                             size) 


#     for item in filelist2:
#         # print(item)
#         if item.endswith('.jpg'):
#             # print(item)
#             img = cv2.imread(item)
#             video.write(img)

#     video.release()
#     cv2.destroyAllWindows()
#     print('DONE')

def frame2video(path, mode = 0):

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

    out = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
    
    if mode == 1:
        video = cv2.VideoWriter(path + "/Video.mp4", cv2.VideoWriter_fourcc('m','p','4','v'), fps,
                            size) 

    elif mode == 0:
        video = cv2.VideoWriter('/Users/songminglun/Documents/ILCS/ilcs_5/slib/slib_img/saved_video/' + str(out) + '.mp4', cv2.VideoWriter_fourcc('m','p','4','v'), fps,
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
    imshow('/Users/songminglun/Documents/ILCS/2021/MTG資料/0521/video/kurita_001/video_3')
