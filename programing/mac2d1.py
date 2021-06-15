import glob


from func import cp

def main(folder_path, tgt):

    folders = sorted(glob.glob(folder_path + '/*'))

    for folder in folders:

        files = sorted(glob.glob(folder + '/video/*'))

        for i in files:

            folder_name = i.split('/')[-1]

            cp('-r', i, tgt + '/' + folder_name)




if __name__ == '__main__':
    main('/Users/songminglun/Documents/ILCS/2021/dataset/data', '/Users/songminglun/Documents/ILCS/ilcs_5/test')