import random
import numpy as np
import os
from scipy import io as sio
import re


def dilate(input_mat, out_size):
    dial_vec = random.sample(range(input_mat.shape[1]), out_size)
    dial_vec.sort()
    dilated_mat = input_mat[:, dial_vec]
    return dilated_mat


def DilateAll(folder_name, out_size):
    for file_name in os.listdir(folder_name):
        if re.search(r".*.mat", file_name):
            file = sio.loadmat(folder_name + '/' + file_name)
            file_data = file['image_data']
            new_file = dilate(file_data, out_size)
            sio.savemat(folder_name + '/new' + out_size.__str__() + '/' + file_name, {'new_file': new_file})
        else:
            match = re.search(r"(.*).bmpLR", file_name)
            if match:
                new_name = folder_name + '/images/' + match.group(1) + '.bmp'
                os.rename(folder_name + '/' + file_name, new_name)


if __name__ == '__main__':
    for i in {64, 32, 16}:
        DilateAll('/home/yonipeleg/PycharmProjects/UltraSound/image', i)
