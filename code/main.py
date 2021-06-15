# meirin sou

import glob


import func.keypoints_from_images as kfi
import slib_os as so
import func.frame2video as fv
import func.video2frame as vf


def makedir(path_video):
    dir_name = path_video.split('/')[-1]
    dir_name = dir_name.split('.')[0]
    path_video_dir = so.merge(path_video.split('/')[:-1]) + '/' + dir_name
    so.mkdir(path_video_dir)
    return path_video_dir


def video_estimation(folder_path):
    # path_video_dir = makedir(path_video)# create a dir which name is as same as video's

    so.mkdir(folder_path + '/video_1')
    so.mkdir(folder_path + '/video_2')
    so.mkdir(folder_path + '/data')# creat dir: video_1 video_2 data

    folder_name = folder_path.split('/')[-1]

    video_path = folder_path + '/' + folder_name + '.mp4'


    vf.video2frame(video_path, folder_path + '/video_1')# video to frame


    kfi.keypoints_from_images(folder_path + '/video_1', 
    folder_path + '/video_2', 
    folder_path + '/data')# detect human keypoints and outup images

    # kfic.keypoints_from_images(folder_path + '/video_1', 
    # folder_path + '/video_2', 
    # folder_path + '/data')# detect human keypoints and outup images

    fv.frame2video(folder_path + '/video_2')

    so.mv(video_path, folder_path + '/')

# def videos_estimation(path_file):

#     files = sorted(glob.glob(path_file + '/*.mp4'))
    
#     for i in files:

#         video_estimation(i)

def main(folder_path):

    folders = sorted(glob.glob(foder_path + '/*'))

    for folder in folders:

if __name__ == '__main__':
    main('/home/ilcs/openpose/examples/tutorial_api_python/code/video')

