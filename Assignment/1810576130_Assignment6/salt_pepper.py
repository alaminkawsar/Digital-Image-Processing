'''Assignment 6 Done'''


'''URL of some tutorials'''
#https://opencv24-python-tutorials.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_filtering/py_filtering.html


import cmath
import matplotlib.pyplot as plt
import cv2
import numpy as np


def main():
    
    #Load an RGB image from a image_path
    img_path = '/home/kawsar/Desktop/Class_Resource/4th year 1st semester/4181- Digital Image Processing/ImageProcessingLab/Assignment/1810576130_Assignment6/rose.jpg'
    #img_path = '/home/kawsar/Desktop/Class_Resource/4th Year 1st semester/ImageProcessingLab/Assignment/1810576130_Assignment6/flower.jpeg'
    #print(img_path)
    rgb = plt.imread(img_path)
    #print(rgb)
    
    #Split loaded RGB image into grayscale, red, green, blue and binary image
    
    x, y = 2,3
    pos, channel = 1, 0
    for i in range(10):
        print(np.random.randint(10,20))
    plt.figure(figsize=(20,20))
    
    title = ['Grayscale Image','Filtered Image\n(Averaging)','Noisy Image\n(Salt and Pipper Noise)',
             'Filtered Noisy Image\n(Averaging)','Filtered Noisy Image\n(Gaussian Kernel)',
             'Filtered Noisy Image\n(Median Kernel)']
    image = []
    
    grayscale = cv2.cvtColor(rgb, cv2.COLOR_RGB2GRAY)
    grayscale = cv2.resize(grayscale, (580,480))
    
    image.append(grayscale)
    
    '''Filtered Image(Averaging)'''
    kernel_average = np.ones((3, 3), dtype = int)/9
    filtered_average = cv2.filter2D(grayscale,-1,kernel_average)
    image.append(filtered_average)


    
    '''Let's take 3000 number of random pixel positions'''
    w, h = grayscale.shape
    noisyImage = np.copy(grayscale)
    numbersOfPixel = 3000
    noisy_X = np.random.randint(w,size=numbersOfPixel)
    noisy_Y = np.random.randint(h,size=numbersOfPixel)
    
    
    for i in range(numbersOfPixel):
        binary_pixel = np.random.randint(0,2)
        noisyImage[noisy_X[i],noisy_Y[i]]=binary_pixel*255
    
    image.append(noisyImage)
    
    
    '''Filtered Noisy Image(Averaging)'''
    kernel_average = np.ones((3, 3), dtype = int)/9
    noisy_filtered_average = cv2.filter2D(noisyImage,-1,kernel_average)
    image.append(noisy_filtered_average)
    
    
    '''Filtered using Gaussian kernel'''
    gaussian_kernel = np.array([[1,2,1],
                                [2,4,2],
                                [1,2,1]])/16
    gaussian = cv2.filter2D(noisyImage,-1,gaussian_kernel)
    #gaussian = cv2.GaussianBlur(noisyImage,(3,3),0)
    image.append(gaussian)
    
    
    '''Filtered using Median'''
    median = cv2.medianBlur(noisyImage,3)
    image.append(median)

    
    
    '''Show all of Image with subplot'''
    for pos in range(len(image)):
        plt.subplot(x,y,pos+1)
        plt.title(title[pos])
        plt.imshow(image[pos],cmap='gray')

    
    plt.show()
    plt.savefig("/home/kawsar/Desktop/Class_Resource/4th Year 1st semester/ImageProcessingLab/Assignment/1810576130_Assignment6/salt_pepper.png")

    
if __name__ == '__main__':
	main()