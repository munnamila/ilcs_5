import os


def mkdir(dir_name):
    isExists = os.path.exists(dir_name)

    if not isExists:
        os.makedirs(dir_name)
    
    else:
        print('File exists')

def mv(src, tgt):
    os.system('mv ' + src + ' ' + tgt)

def merge(lists):

    new_path = '/'

    for i in lists:

        new_path = os.path.join(new_path, i)

    return new_path

if __name__ == '__main__':
    pass
