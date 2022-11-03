import numpy as np

def sort_by_frequency(arr):
    return np.flip(np.argsort(np.bincount(arr))[-(np.unique(arr).size):])
    # np.flip - 
    # np.argsort - 
    # np.unique -

def main_func():
    v = [int(i) for i in input().split()]
    print(sort_by_frequency(v))

main_func()