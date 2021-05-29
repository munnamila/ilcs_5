# 2021/5/29
# SOU Meirin


import cv2
import numpy as np
import glob


def pose2plot(pose, screen):
    # input: keypoint of body25 from openpose, screen
    # output: show keypoint

    len_pose = pose.shape[1]

    for i in range(len_pose):

        if pose[0,i,0] == 0:
            continue

        else:
            x = pose[0, i, 0]
            y = pose[0, i, 1]
            n = pose[0, i, 2] * 255
            cv2.circle(screen, ((x/2).astype(np.float32), (y/2).astype(np.float32)), 3, (0, n, 255-n), -1)# origin
            # cv2.circle(canvas, (pose[0,i,0], pose[0,i,1]), 2, (255, 255, 255), -1)
            # screen = cv2.resize(screen, (640, 360))
        
    cv2.imshow('test', screen)
    cv2.waitKey(1)

def pose2plot_seikika(pose, screen):
    # input: keypoint of body25 from openpose, screen
    # output: show keypoint normalized

    len_pose = pose.shape[1]

    for i in range(len_pose):

        dx = pose[0, 1, 0] - 640
        dy = pose[0, 1, 1] - 320

        if pose[0,i,0] == 0:
            continue

        else:
            x = pose[0, i, 0]
            y = pose[0, i, 1]
            n = pose[0, i, 2] * 255

            cv2.circle(screen, (((x - dx) / 2).astype(np.float32), ((y - dy) / 2).astype(np.float32)), 3, (0, n, 255 - n), -1)


        
    cv2.imshow('test_', screen)
    cv2.waitKey(1)
