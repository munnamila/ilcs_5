# author: sou meirin
# this code is for processing time series data

import numpy as np

def moving_average(time_series_data, widow_size):
    # input data is allowed to be list or numpy.array
    # the output size is as same as input size
    # widow_size is required to be singular and 1<widow_size

    # checking window size
    if widow_size % 2 == 0:
        print('Sou: Error! window_size is required to be singular! ')
        return -1

    if widow_size <= 0:
        print('Sou: Error! window_size is required to be greater than 0! ')

    widow_size_half = widow_size//2

    output_list = []

    for i in range(len(time_series_data)):

        if i-widow_size_half < 0:
            new_value = np.array([j for j in time_series_data[: i+widow_size_half+1]]).mean()

        elif i+widow_size_half+1 > len(time_series_data)-1:
            new_value = np.array([j for j in time_series_data[i-widow_size_half: ]]).mean()

        else:
            # calculate new value
            new_value = np.array([j for j in time_series_data[i-widow_size_half: i+widow_size_half+1]]).mean()

        output_list.append(new_value)

    return output_list



if __name__ == '__main__':
    print(moving_average([1, 2, 3, 4, 5], -1))