import cv2

def main(src, tgt):

    cap = cv2.VideoCapture(src)

    count = 0

    while 1:
        ret, frame = cap.read()

        cv2.imwrite(tgt + "/" + str('%06d' % count) + ".jpg", frame)
        count += 1

    cap.release()

if __name__ == '__main__':
    main('lab_introduction.mp4', 'lab_introduction')
