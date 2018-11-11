import random
import numpy as np
import os
from scipy import io as sio


def dilate(input_mat, out_size):
    dial_vec = random.sample(range(input_mat.shape[1]), out_size)
    dial_vec.sort()
    return input_mat[:, dial_vec]


def DilateAll(folder_name, out_size):
    for file in os.listdir(folder_name):
        sio.savemat('new' + file.__str__(), dilate(file, out_size))


if __name__ == '__main__':
    a = np.random.randint(100, size=(5, 5))
    b = dilate(a, 3)
