import os

def cp(mode, src, tgt):
    isExists = os.path.exists(tgt)
    if not isExists:

        if mode == '-r':
            os.system('cp ' + '-r ' +  src + ' ' + tgt)

        else:
            os.system('cp ' +  src + ' ' + tgt)

    else:
        print('File or folder exists')
