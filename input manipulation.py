import random
import numpy as np


def dilate(in_size, out_size):
    return random.sample(set(range(in_size)), out_size)