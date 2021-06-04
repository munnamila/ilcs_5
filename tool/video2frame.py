# 2021/5/12
# sou meirin
# Done


import cv2

def video2frame(src, tgt):

    cap = cv2.VideoCapture(src)

    count = 0

    while 1:

        ret, frame = cap.read()

        if ret:
            cv2.imwrite(tgt + "/" + str('%06d' % count) + ".jpg", frame)
            count += 1

        else:
            break

    cap.release()

if __name__ == '__main__':
    video2frame('/Users/songminglun/Documents/ILCS/murase/murase.mp4', '/Users/songminglun/Documents/ILCS/murase/murase')
    print('Done')

