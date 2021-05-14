import glob

import sys
sys.path.append('../../../..')
import ilcs_5.slib.slib_os.slib_os as so
import ilcs_5.tool.frame2video
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

    print('done')

if __name__ == '__main__':
    main('/home/flowerdance/openpose/examples/media/video/murase.mp4')