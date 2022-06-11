#https://betterdatascience.com/implement-convolutions-from-scratch-in-python/

from pickletools import int4
import numpy as np

def main():
    mat1 = np.array([
        [1,2,3],
        [6,7,8],
        [11,12,13],
    ])
    mat2 = np.array([
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ])   
    new_mat = np.multiply(mat1,mat2)
    print(new_mat)

if __name__ == '__main__':
    main()