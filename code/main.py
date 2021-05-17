# meirin sou

import glob


import keypoint_from_images as kfi
import sys
sys.path.append('../../../..')
import ilcs_5.slib.slib_os.slib_os as so
import ilcs_5.tool.frame2video as fv
import ilcs_5.tool.video2frame as vf


def makedir(path_vidoe):
    dir_name = path_vidoe.split('/')[-1]
    dir_name = dir_name.split('.')[0]
    path_vidoe_dir = so.merge(path_vidoe.split('/')[:-1]) + '/' + dir_name
    so.mkdir(path_vidoe_dir)
    return path_vidoe_dir


def main(path_vidoe):
    path_vidoe_dir = makedir(path_vidoe)# create a dir which name is as same as video's

    so.mkdir(path_vidoe_dir + '/video_1')
    so.mkdir(path_vidoe_dir + '/video_2')
    so.mkdir(path_vidoe_dir + '/data')# creat dir: video_1 video_2 data

    vf.video2frame(path_vidoe, path_vidoe_dir + '/video_1')# video to frame

    

    kfi.keypoints_from_images(path_vidoe_dir + '/video_1', 
    path_vidoe_dir + '/video_2', 
    path_vidoe_dir + '/data')# detect human keypoints and outup images

    fv.frmae2video(path_vidoe_dir + '/video_2', (w, h))# 自動的に画像のサイズを検出することが必要、今は手動で記入


    print('done')

if __name__ == '__main__':
    main('/home/flowerdance/openpose/examples/media/video/murase.mp4')