# 2021/5/29
# SOU Meirin


import cv2
import numpy as np
import glob
import os


def pose2plot(pose, screen):
    # input: keypoint of body25 from openpose, screen
    # output: show keypoint



    try:

        len_pose = pose.shape[1]

        for i in range(len_pose):

            if pose[0,i,0] == 0:
                    continue

            else:
                    x = int(pose[0, i, 0])
                    y = int(pose[0, i, 1])
                    n = int(pose[0, i, 2] * 255)
                    cv2.circle(screen, (x, y), 3, (0, n, 255-n), -1)# origin
                    # cv2.circle(canvas, (pose[0,i,0], pose[0,i,1]), 2, (255, 255, 255), -1)
                    # screen = cv2.resize(screen, (640, 360))

    except:
        pass
        
    cv2.imshow('test', screen)
    cv2.waitKey(1)


def pose2plot_seikika(pose, screen):
    # input: keypoint of body25 from openpose, screen
    # output: show keypoint normalized

    try:

        len_pose = pose.shape[1]

        for i in range(len_pose):

            dx = int(pose[0, 1, 0] - 640)
            dy = int(pose[0, 1, 1] - 320)

            if pose[0,i,0] == 0:
                continue

            else:
                x = int(pose[0, i, 0])
                y = int(pose[0, i, 1])
                n = int(pose[0, i, 2] * 255)

                # cv2.circle(screen, (((x - dx) / 2).astype(np.float32), ((y - dy) / 2).astype(np.float32)), 3, (0, n, 255 - n), -1)
                cv2.circle(screen, (x-dx-320, y-dy), 3, (0, n, 255-n), -1)# origin


    except:
        pass

    cv2.imshow('test_', screen)
    cv2.waitKey(1)

def frame2video(path):

    path_img = sorted(glob.glob(path + '/*'))[0]
    img = cv2.imread(path_img)
    size_img = img.shape
    w = size_img[1]
    h = size_img[0]

    size = (w, h)

    filelist = os.listdir(path)
    filelist2 = [os.path.join(path, i) for i in filelist]
    filelist2 = sorted(filelist2)
    # print(filelist2)
    fps = 30  
    video = cv2.VideoWriter(path + "/Video.avi", cv2.VideoWriter_fourcc('M','J','P','G'), fps,
                            size) 

    for item in filelist2:
        # print(item)
        if item.endswith('.jpg'):
            # print(item)
            img = cv2.imread(item)
            video.write(img)

    video.release()
    cv2.destroyAllWindows()
    print('DONE')

def keypoints_from_images(src, tgt_imgs, tgt_points):
    try:
        # Import Openpose (Windows/Ubuntu/OSX)
        dir_path = os.path.dirname(os.path.realpath(__file__))
        try:
            # Windows Import
            if platform == "win32":
                # Change these variables to point to the correct folder (Release/x64 etc.)
                sys.path.append(dir_path + '/../../python/openpose/Release');
                os.environ['PATH']  = os.environ['PATH'] + ';' + dir_path + '/../../x64/Release;' +  dir_path + '/../../bin;'
                import pyopenpose as op
            else:
                # Change these variables to point to the correct folder (Release/x64 etc.)
                sys.path.append('../../../build/python');
                # If you run `make install` (default path is `/usr/local/python` for Ubuntu), you can also access the OpenPose/python module from there. This will install OpenPose and the python library at your desired installation path. Ensure that this is in your python path in order to use it.
                # sys.path.append('/usr/local/python')
                from openpose import pyopenpose as op
        except ImportError as e:
            print('Error: OpenPose library could not be found. Did you enable `BUILD_PYTHON` in CMake and have this Python script in the right folder?')
            raise e

        # Flags
        parser = argparse.ArgumentParser()
        parser.add_argument("--image_dir", default=src, help="Process a directory of images. Read all standard formats (jpg, png, bmp, etc.).")
        parser.add_argument("--no_display", default=False, help="Enable to disable the visual display.")
        args = parser.parse_known_args()



        # Custom Params (refer to include/openpose/flags.hpp for more parameters)
        params = dict()
        params["model_folder"] = "../../../models/"
        params["face"] = True
        params["hand"] = True

        # Add others in path?
        for i in range(0, len(args[1])):
            curr_item = args[1][i]
            if i != len(args[1])-1: next_item = args[1][i+1]
            else: next_item = "1"
            if "--" in curr_item and "--" in next_item:
                key = curr_item.replace('-','')
                if key not in params:  params[key] = "1"
            elif "--" in curr_item and "--" not in next_item:
                key = curr_item.replace('-','')
                if key not in params: params[key] = next_item

        # Construct it from system arguments
        # op.init_argv(args[1])
        # oppython = op.OpenposePython()

        # Starting OpenPose
        opWrapper = op.WrapperPython()
        opWrapper.configure(params)
        opWrapper.start()

        # Read frames on directory
        imagePaths = op.get_images_on_directory(args[0].image_dir);
        start = time.time()

        # Process and display images

        count = 0

        for imagePath in tqdm(imagePaths):
            datum = op.Datum()
            imageToProcess = cv2.imread(imagePath)
            datum.cvInputData = imageToProcess
            opWrapper.emplaceAndPop(op.VectorDatum([datum]))

            # print("Body keypoints: \n" + str(datum.poseKeypoints))
            np.savez(tgt_points + '/' + '%06d' % count + '.npz', pose = datum.poseKeypoints, face = datum.faceKeypoints, hand_left = datum.handKeypoints[0], hand_right = datum.handKeypoints[1])

            if not args[0].no_display:
                # cv2.imshow("OpenPose 1.7.0 - Tutorial Python API", datum.cvOutputData)
                cv2.imwrite(tgt_imgs+ '/' + '%06d' % count + '.jpg', datum.cvOutputData)
                # key = cv2.waitKey(1)
                # if key == 27: break
            count += 1

        end = time.time()
        print("OpenPose demo successfully finished. Total time: " + str(end - start) + " seconds")
    except Exception as e:
        print(e)
        sys.exit(-1)

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
    pass
