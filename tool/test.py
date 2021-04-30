import argparse

def main(x):

    print('img path is:' + x)

if __name__ == '__main__':
    # parser = argparse.ArgumentParser()
    # parser.add_argument('--image_path', default = '/123/123_jpg', help = '123')
    # args = parser.parse_known_args()
    # print(type(args))
    # print(args)
    # print(args[0])
    # # main(args)

    parser = argparse.ArgumentParser(description='123')
    parser.add_argument('--path', type = str, help='13')
    parser.add_argument('--size', type = list, help = 'size' )

    args = parser.parse_args()
    print(args.path)
    print(args.size)
    

