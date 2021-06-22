import glob
import numpy as np
from tqdm import tqdm

def opticflow(x1, y1, x2, y2):
    
    # caculate the optic flow of 2 opints
    # return dx dy
    # checked
    
    dx = x2 - x1
    dy = y2 - y1
    
    return dx, dy

def get_opticflow(data_before, data, model, kp_num, people_num = 0):
    
    # one people
    # get dx, dy from 2 frames
    # checked
    
    if data[model][people_num, kp_num, 2] != 0 and data_before[model][people_num, kp_num, 2] != 0:
        # if curray is not 0
        x2 = data[model][people_num, kp_num, 0]
        y2 = data[model][people_num, kp_num, 1]

        x1 = data_before[model][people_num, kp_num, 0]
        y1 = data_before[model][people_num, kp_num, 1]

        dx, dy = opticflow(x1, y1, x2, y2)

#         out = [dx, dy]
        
    else:
#         out = None
        dx = dy = 0
    
    return dx, dy

def get_coordinate(data, model, kp_num, people_num = 0):
    
    # one people
    # get coordinate from one frame
    # checked
    
    if data[model][people_num, kp_num, 2] != 0:
        
        x = data[model][people_num, kp_num, 0]
        y = data[model][people_num, kp_num, 1]
        
#         out = [x, y]
        
    else:
#         out = None
        x = y = None
    
    return x, y

def load_FV(folder):
    # folder: W2_6_000000/

    files = sorted(glob.glob(folder + '/data/*'))

    data_before = None

    out_list = []

    first_data = np.load(files[0])

    body1_x, body1_y = get_coordinate(first_data, 'pose', 1)
    body8_x, body8_y = get_coordinate(first_data, 'pose', 8)

    rate = 300 / ((body1_x - body8_x)**2 + (body1_y - body8_y)**2)**(1/2)

    



    

    for i in files:
        # i: 000000.npz
        data = np.load(i)

        body1_x, body1_y = get_coordinate(data, 'pose', 1)
        body8_x, body8_y = get_coordinate(data, 'pose', 8)


        if data_before != None:

            FV_1_dx, FV_1_dy = get_opticflow(data_before, data, 'pose', 4)
            FV_2_dx, FV_2_dy = get_opticflow(data_before, data, 'pose', 7)
            FV_3_dx, FV_3_dy = get_opticflow(data_before, data, 'pose', 3)
            FV_4_dx, FV_4_dy = get_opticflow(data_before, data, 'pose', 6)

            FV_5_dx, FV_5_dy = get_coordinate(data, 'pose', 4)
            FV_6_dx, FV_6_dy = get_coordinate(data, 'pose', 7)
            FV_7_dx, FV_7_dy = get_coordinate(data, 'pose', 3)
            FV_8_dx, FV_8_dy = get_coordinate(data, 'pose', 6)

            FV_5_dx, FV_5_dy = FV_5_dx - body1_x, FV_5_dy - body1_y
            FV_6_dx, FV_6_dy = FV_6_dx - body1_x, FV_6_dy - body1_y
            FV_7_dx, FV_7_dy = FV_7_dx - body1_x, FV_7_dy - body1_y
            FV_8_dx, FV_8_dy = FV_8_dx - body1_x, FV_8_dy - body1_y

            FV_9_dx, FV_9_dy = get_opticflow(data_before, data, 'pose', 1)
            FV_10_dx, FV_10_dy = get_opticflow(data_before, data, 'pose', 0)

        else:
            FV_1_dx = FV_1_dy = FV_2_dx =  FV_2_dy = FV_3_dx = FV_3_dy = FV_4_dx = FV_4_dy = FV_9_dx = FV_9_dy = FV_10_dx = FV_10_dy = 0
            
            
            FV_5_dx, FV_5_dy = get_coordinate(data, 'pose', 4)
            FV_6_dx, FV_6_dy = get_coordinate(data, 'pose', 7)
            FV_7_dx, FV_7_dy = get_coordinate(data, 'pose', 3)
            FV_8_dx, FV_8_dy = get_coordinate(data, 'pose', 6)
            
            FV_5_dx, FV_5_dy = FV_5_dx - body1_x, FV_5_dy - body1_y
            FV_6_dx, FV_6_dy = FV_6_dx - body1_x, FV_6_dy - body1_y
            FV_7_dx, FV_7_dy = FV_7_dx - body1_x, FV_7_dy - body1_y
            FV_8_dx, FV_8_dy = FV_8_dx - body1_x, FV_8_dy - body1_y
            
            
        out = np.array([FV_1_dx, FV_1_dy, FV_2_dx, FV_2_dy, FV_3_dx, FV_3_dy, FV_4_dx, FV_4_dy, FV_5_dx, FV_5_dy, FV_6_dx, FV_6_dy, FV_7_dx, FV_7_dy, FV_8_dx, FV_8_dy, FV_9_dx, FV_9_dy, FV_10_dx, FV_10_dy]) * rate
        
        data_before = data

        out_list.append(out)

    out_list = np.array(out_list)

    return out_list

        


    



def load_dataset(video_path):

    folders = sorted(glob.glob(video_path + '/*'))

    labels = []
    fv_list = []
    name_list = []

    print('loading dataset ...')

    for folder in tqdm(folders):
        # folder: W2_6_000000/

        folder_name = folder.split('/')[-1]

        with open(folder + '/label.txt', 'r') as f:
            label = f.read()


        if label == '手を回転させる':
            labels.append(0)
            fv = load_FV(folder)
            fv_list.append(fv)
            name_list.append(folder_name)


        elif label == '黒板で手をスライドさせる':
            labels.append(1)
            fv = load_FV(folder)
            fv_list.append(fv)
            name_list.append(folder_name)

        elif label == '黒板に指す':
            labels.append(2)
            fv = load_FV(folder)
            fv_list.append(fv)
            name_list.append(folder_name)

        else:
            pass


    y = np.array(labels)
    x = np.array(fv_list)
    name = np.array(name_list)

    return x, y, name






if __name__ == '__main__':
    x, y, name = load_dataset('/Users/songminglun/Documents/ILCS/data/video')
    np.save('/Users/songminglun/Documents/ILCS/data/label.npy', y)
    np.save('/Users/songminglun/Documents/ILCS/data/path_name.npy', name)
    np.save('/Users/songminglun/Documents/ILCS/data/feature_value.npy', x)

