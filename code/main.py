# meirin sou

import glob


import keypoints_from_images as kfi
import keypoints_from_images_coco as kfic
import slib_os as so
import frame2video as fv
import video2frame as vf


def makedir(path_video):
    dir_name = path_video.split('/')[-1]
    dir_name = dir_name.split('.')[0]
    path_video_dir = so.merge(path_video.split('/')[:-1]) + '/' + dir_name
    so.mkdir(path_video_dir)
    return path_video_dir


def video_estimation(path_video):
    path_video_dir = makedir(path_video)# create a dir which name is as same as video's

    so.mkdir(path_video_dir + '/video_1')
    so.mkdir(path_video_dir + '/video_2')
    so.mkdir(path_video_dir + '/data')# creat dir: video_1 video_2 data


    vf.video2frame(path_video, path_video_dir + '/video_1')# video to frame

    

    # kfi.keypoints_from_images(path_video_dir + '/video_1', 
    # path_video_dir + '/video_2', 
    # path_video_dir + '/data')# detect human keypoints and outup images

    kfic.keypoints_from_images(path_video_dir + '/video_1', 
    path_video_dir + '/video_2', 
    path_video_dir + '/data')# detect human keypoints and outup images

    fv.frame2video(path_video_dir + '/video_2')

    so.mv(path_video, path_video_dir + '/')

def videos_estimation(path_file):

    files = sorted(glob.glob(path_file + '/*.mp4'))
    
    for i in files:

        video_estimation(i)


if __name__ == '__main__':
    videos_estimation('/home/ilcs/openpose/examples/tutorial_api_python/code/video')

