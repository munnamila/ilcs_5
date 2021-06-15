import cv2



cap = cv2.VideoCapture(1)

while 1:

    ret, frame = cap.read()

    cv2.imshow('frame', frame)

    if cv2.waitKey(100) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()



