import cv2

def test():
    print('You already can use slib_video')

def summary(video_path, info=True):
    cap = cv2.VideoCapture(video_path)
    width = int(cap.get(3))# width
    hight = int(cap.get(4))# hight
    frame_rate = cap.get(5)
    video_time = cap.get(7) / frame_rate
    video_time_s = format(video_time, '.2f')
    video_time_min = format(video_time/60, '.2f')
    video_time_h = format(video_time/3600, '.2f')

    if info == True:
        print(' ')
        print('====================video_summary==========================================================')
        print('path of video: ', video_path)
        print('The width of this video: ' + str(width) + 'pixcel')
        print('The hight of this video: ' + str(hight) + 'pixcel')
        print('The frame_rate of this video: ' + str(frame_rate) + 'fps')
        print('The video_time of this video: ' + video_time_s + 's | ' + video_time_min + 'min | ' + video_time_h + 'h')
        print('===========================================================================================')
        print(' ')

    return width, hight, frame_rate, video_time_s


if __name__ == '__main__':
    import glob
    path = '/Volumes/HDPH-UT/video'
    folders = sorted(glob.glob(path + '/*'))
    for folder in folders:
        if 'xlsx' in folder:
            pass
        else:
            files = sorted(glob.glob(folder + '/*'))
            for file in files:
                data = sorted(glob.glob(file + '/*'))
                for i in data:
                    try:
                        summary(i)
                    except:
                        pass