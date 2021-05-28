import os
import glob
from tqdm import tqdm

import slib_os as so
        

def mkdir_and_get_keypoint(video_path):

    dir_name = video_path.split('/')[-1]
    dir_name = dir_name.split('.')[0]
    dir_name = so.merge(video_path.split('/')[:-1]) + '/' + dir_name


    so.mkdir(dir_name)
    so.mkdir(dir_name + '/video')
    so.mkdir(dir_name + '/data')


    # move the video
    so.mv(video_path, dir_name + '/video/')

def main(dir):
    files = sorted(glob.glob(dir + '/*'))

    for i in tqdm(files):
        mkdir_and_get_keypoint(i)


if __name__ == '__main__':
    main('/Users/songminglun/Documents/ILCS/code/02_prepropocessing/video')
    # mkdir_and_get_keypoint('/Users/songminglun/Documents/ILCS/code/02_prepropocessing/video/lab_introduction.mp4')

    