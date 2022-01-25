# 2021/5/12
# sou meirin
# Done


import cv2

def video2frame(src, tgt):

    cap = cv2.VideoCapture(src)

    # get fps
    fps = int(cap.get(5) + 0.5)

    count = 0

    while 1:

        ret, frame = cap.read()

        if ret:
            cv2.imwrite(tgt + "/" + str('%06d' % count) + ".jpg", frame)
            count += 1

        else:
            break

    cap.release()
    return fps

if __name__ == '__main__':
    video2frame('/Users/songminglun/Documents/ILCS/murase/murase.mp4', '/Users/songminglun/Documents/ILCS/murase/murase')
    print('Done')

