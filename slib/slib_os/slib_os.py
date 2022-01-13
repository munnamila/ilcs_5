import os
import glob

def test():
    # test
    # slib_os.test()
    # done
    print('You already can use slib_os!!!!')

def mkdir(dir_name):
    # create a dir
    # slib_os.mkdir('test/')
    # done
    isExists = os.path.exists(dir_name)

    if not isExists:
        os.makedirs(dir_name)
    else:
        pass

def mv(src, tgt):
    # move file or dir
    # slib_os.mv('dir1/test', 'dir2/')
    os.system('mv ' + src + ' ' + tgt)

def cp(src, tgt, mode= None):
    if mode == '-r':
        os.system('cp ' + '-r ' +  src + ' ' + tgt)

    else:
        os.system('cp ' + src + ' ' + tgt)


def merge(lists):

    new_path = '/'

    for i in lists:

        new_path = os.path.join(new_path, i)

    return new_path


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
