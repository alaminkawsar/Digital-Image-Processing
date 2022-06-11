#https://betterdatascience.com/implement-convolutions-from-scratch-in-python/

from pickletools import int4
import numpy as np

def main():
    mat = np.array([
        [1,2,3,4,5],
        [6,7,8,9,10],
        [11,12,13,14,15],
        [16,17,18,19,20],
        [21,22,23,24,25]
    ])    
    '''Let's do matrix operation using slicing'''
    k = 3
    w, h = mat.shape
    new_mat = np.zeros((w-k+1,h-k+1),dtype=int)
    for i in range(0,w-k+1):
        for j in range(0,h-k+1):
            s= np.sum(mat[i:i+k,j:j+k])
            print(s,end=' ')
            new_mat[i,j]=s
        print()
    
    print(new_mat)    

if __name__ == '__main__':
    main()