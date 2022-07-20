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

    def change_files_in_dir_to_counting(src, number_of_digits):
        # 把文件夹里的文件，按数字顺重命名
        # src: 文件夹的路径
        # number_of_digits: 数位
        # doing

        files = sorted(glob.glob(src + '/*'))

        for num, i in enumerate(files):

            os.system('mv ' + str(i) + ' ' + '%06d' % num)


def time_transform(input_time):
    # second to time
    # 3600 => 01:00:00

    min = 60
    hour = 60 * 60

    HOUR = input_time // hour
    MINUT = (input_time - (HOUR * hour)) // min
    SECONDS = input_time - ((HOUR * hour) + (MINUT * min))

    print('{}:{}:{}'.format('%02d' % HOUR, '%02d' %MINUT, '%02d' %SECONDS))



    



    


if __name__ == '__main__':
    # release_files('/Users/songminglun/Desktop/test的副本')
    time_transform(99010)
