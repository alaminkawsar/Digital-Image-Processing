import numpy as np
import cv2 
import matplotlib.pyplot as plt

def countOne(kernel):
    cnt = 0
    _, k = kernel.shape
    for i in range(k):
        for j in range(k):
            if(kernel[i][j]>0):
                cnt += 1
    return cnt

def padding(img:np.array)->np.array:
    w, h = img.shape
    new_img = np.zeros(shape=(w+2,h+2))
    w, h = new_img.shape
    new_img[1:w-1,1:h-1] = img
    new_img.astype(int)
    return new_img

def erosion(img: int, kernel: int)->np.array:
    img = padding(np.array(img))
    _, k = kernel.shape
    w, h = img.shape
    new_w, new_h = w-k+1, h-k+1
    conv_img = np.zeros(shape=(new_w,new_h))
    
    
    # number of one count
    cnt = countOne(kernel=kernel)
    #print(cnt)
    for i in range(new_w):
        for j in range(new_h):
            mat = img[i:i+k,j:j+k]
            flag = countOne(np.multiply(kernel,mat))
            
            if flag==cnt:
                conv_img[i,j]=1
            else:
                conv_img[i,j]=0;
    return conv_img

def dilation(img: int, kernel: int)->np.array:
    img = padding(np.array(img))
    _, k = kernel.shape
    w, h = img.shape
    new_w, new_h = w-k+1, h-k+1
    conv_img = np.zeros(shape=(new_w,new_h))
    
    #number of one count
    cnt = countOne(kernel=kernel)
    #print(cnt)
    for i in range(new_w):
        for j in range(new_h):
            mat = img[i:i+k,j:j+k]
            flag = countOne(np.multiply(kernel,mat))
            
            if flag>0:
                conv_img[i,j]=1
            else:
                conv_img[i,j]=0;
    return conv_img


img_path = '/home/kawsar/Desktop/Class_Resource/4th year 1st semester/4181- Digital Image Processing/ImageProcessingLab/Assignment/1810576130_Assignment9/tree.jpg'
img = cv2.imread(img_path,0)

#img = cv2.resize(img,(300,300))
_, img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

x, y, pos = 1, 3, 1
List = []
List.append([img,'Main Image'])

# Taking a matrix of size 5 as the kernel
kernel1 = np.ones((3, 3), np.uint8)


#Built in dilation
img_dilation = cv2.dilate(img,kernel1, iterations=1)
List.append([img_dilation,'Built in Dilation Image'])
#custom dilation
custom_dilation = dilation(img, kernel1)
List.append([custom_dilation,'Custom Dialtion Image'])

#Built in opening image



for im, title in List:
    plt.subplot(x, y, pos)
    plt.title(title)
    plt.imshow(im,cmap='binary')
    pos += 1

plt.show()