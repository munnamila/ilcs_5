import os
import glob

def test():
    print('You already can use slib_os!!!!')

def mkdir(dir_name):
    isExists = os.path.exists(dir_name)

    if not isExists:
        os.makedirs(dir_name)
    
    else:
        pass

def mv(src, tgt):
    os.system('mv ' + src + ' ' + tgt)

def cp(mode, src, tgt):
    if mpde == '-r':
        os.system('cp ' + '-r ' +  src + ' ' + tgt)

    else:
        os.system('cp ' + src + ' ' + tgt)


def merge(lists):

    new_path = '/'

    for i in lists:

        new_path = os.path.join(new_path, i)

    return new_path

def recreate_video(path_video):
    import cv2

def release_files(src):

    print('starting...')

    files = sorted(glob.glob(src + '/*'))

    tgt = merge(src.split('/')[:-1]) + '/'

    print(tgt)

    for i in files:

        print(i)

        os.system('mv ' + i + ' ' + tgt)

    os.system('rm -r ' + src)

    print('Done')

    



    


if __name__ == '__main__':
    release_files('/Users/songminglun/Desktop/test的副本')
