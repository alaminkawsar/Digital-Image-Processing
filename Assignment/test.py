import numpy as np
import cv2
import matplotlib.pyplot as plt

images = []
titles = []
cmaps = []

def appending(img,title,map):
    images.append(img)
    titles.append(title)
    cmaps.append(map)

def Display():
    n = len(images)
    
    x = int((np.sqrt(n)))
    y = int(np.ceil(n/x))
    for i in range(n):
        plt.subplot(x,y,i+1)
        plt.title(titles[i]) 
        plt.subplot(x,y,i+1)
        plt.title(titles[i])
        if(cmaps[i] == 'hist'):
            plt.hist(images[i].ravel(),256,[0,255])
            continue
        plt.imshow(images[i],cmap=cmaps[i])

def zero_padding (binary_image,struct_element):
    w,h = binary_image.shape
    m,n = struct_element.shape
    padding_image = np.zeros(shape=(w + int(m/2)*2,h + int(n/2)*2))
    w,h = padding_image.shape
    padding_image[int(m/2):w-int(m/2),int(n/2):h-int(n/2)] = binary_image
    return padding_image

def one_padding(binary_image,struct_element):
    w,h = binary_image.shape
    m,n = struct_element.shape
    padding_image = np.zeros(shape=(w + int(m/2)*2,h + int(n/2)*2))
    w,h = padding_image.shape
    padding_image[int(m/2):w-int(m/2),int(n/2):h-int(n/2)] = binary_image
    return padding_image
    
def custom_dilate(binary_image,struct_element):
    padded_image = zero_padding(binary_image,struct_element)
    new_image = np.copy(binary_image)
    m,n = struct_element.shape
    w,h = new_image.shape
    for i in range(w):
        for j in range(h):
            kernel = padded_image[i:i+m,j:j+n]
            new_image[i][j] = np.sum(np.multiply(struct_element,kernel))
            if new_image[i,j] > 0:
                new_image[i,j] = 255
    
    return new_image


def custom_erode(binary_image,struct_element):
    img1 = np.copy(binary_image)
    new_image = np.copy(img1)
    appending(img1,'Binary Image2','binary')
    padded_image = one_padding(binary_image,struct_element)
    m,n = struct_element.shape
    w,h = new_image.shape
    sum = 0
    sum = int(np.sum(struct_element[0:m,0:n]))
    # //print(sum)
    for i in range(w):
        for j in range(h):
            kernel = padded_image[i:i+m,j:j+n]
            new_image[i,j] = np.sum(np.multiply(kernel,struct_element))
            if(sum != new_image[i,j]):
                # print('yes')
                new_image[i,j] = 0
            else:
                new_image[i,j] = 1
    
    return new_image
def main():
    img_path = '/home/kawsar/Desktop/Class_Resource/4th year 1st semester/4181- Digital Image Processing/ImageProcessingLab/Assignment/1810576130_Assignment8/scenery.jpeg'
    img = cv2.imread(img_path,0)
    struct_element = np.ones((5,3))
    
    ret,binary_image = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
    binary_image ^= 255
    erosion_image = cv2.erode(binary_image,struct_element,iterations=1)
    dilation_image = cv2.dilate(binary_image,struct_element,iterations=1)
    
    appending(binary_image,'Binary Image','binary')
    appending(erosion_image,'Built in Erode','binary')
    appending(dilation_image,'Built Dilate Image','binary')

    custom_dilate_image = custom_dilate(binary_image,struct_element)
    custom_erod_image = custom_erode(binary_image,struct_element)

    appending(custom_dilate_image,'Custom Dilate','binary')
    appending(custom_erod_image,'Custom erosion','binary')
    
    # opening_image = cv2.dilate(erosion_image,struct_element,iterations=1)
    # images.append(opening_image)
    # titles.append('Opening Images')
    # closing_image = cv2.erode(dilation_image,struct_element,iterations=1)
    # images.append(closing_image)
    # titles.append('Closing images')

    Display()
    plt.show()
main()