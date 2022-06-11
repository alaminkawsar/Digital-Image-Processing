import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt


def padding(img:np.array)->np.array:
    w, h = img.shape
    new_img = np.zeros(shape=(w+2,h+2))
    w, h = new_img.shape
    new_img[1:w-1,1:h-1] = img
    new_img.astype(int)
    return new_img

def convolute(img: int, kernel: int)->np.array:
    img = padding(np.array(img))
    _, k = kernel.shape
    w, h = img.shape
    new_w, new_h = w-k+1, h-k+1
    conv_img = np.zeros(shape=(new_w,new_h))
    for i in range(new_w):
        for j in range(new_h):
            mat = img[i:i+k,j:j+k]
            conv_img[i,j] = np.sum(np.multiply(kernel,mat))
            if conv_img[i,j]<0:
                conv_img[i,j]=0
            elif(conv_img[i,j]>255):
                conv_img[i,j]=255
    
    return conv_img
    

def main():
    img_path = './image_convolution/flower.jpeg'
    img = cv.imread(img_path,0)
    plt.subplot(2,2,1)
    plt.imshow(img,cmap='gray')
    # plt.imshow(img,cmap='gray')
    # plt.show()
    
    kernel = np.array([
        [3,0,-3],
        [10,0,-10],
        [3,0,-3]
    ])
    
    '''Let's do padding '''
    
    my_kernel_output = convolute(np.array(np.array(img)), kernel)
    kernel_output = cv.filter2D(img,-1, kernel)
    
    
    #print(my_kernel_output.shape,kernel_output.shape)
    print(my_kernel_output.shape,kernel_output.shape)

    #print(new_img,"\n\n\n",img)
    print(my_kernel_output,"\n\n\n",kernel_output)
    
    plt.subplot(2,2,3)
    plt.imshow(my_kernel_output,cmap='gray')
    
    plt.subplot(2,2,4)
    plt.imshow(kernel_output,cmap='gray')
    
    

    
    plt.show()
    
    
    
    

if __name__ == '__main__':
    main()