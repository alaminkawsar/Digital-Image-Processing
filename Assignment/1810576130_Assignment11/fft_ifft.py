from turtle import title
import numpy as np
import cv2 
import matplotlib.pyplot as plt 
import os


def processing():
    img_path = '/home/kawsar/Desktop/Class_Resource/4th year 1st semester/4181- Digital Image Processing/ImageProcessingLab/Assignment/1810576130_Assignment11/nature.jpeg';
    
    image = cv2.imread(img_path,0)
    
    plt.figure(figsize=(20,20))
    dimx, dimy, pos = 3, 2, 1

    fft_img = np.fft.fft2(image)
    fshift = np.fft.fftshift(fft_img)
    mag_fft_img = 20*np.log(np.abs(fshift))
    
    
    img_list = []
    img_list.append([image,"Main Image"]);
    img_list.append([mag_fft_img,"Fourier Transform Image"])
    
    # add mask
    rows, cols = image.shape
    
    crow, ccol = rows//2, cols//2
    
    # Create a mas first, cnter square is 1, remaining all zeros
    mask = np.zeros((rows,cols),np.uint8)
    mask[crow-30:crow+30,ccol-30:ccol+30] = 1
    
    #appy mask and inverse FFT
    ifft_shift = np.fft.ifftshift(fshift*mask)
    mask_ifft = np.fft.ifft2(ifft_shift)
    mag_ifft = 20*np.log(np.abs(mask_ifft))
    
    
    img_list.append([mag_ifft,'After Masking and Applied IFFT Image'])
    
    fft_img = np.fft.fft2(mag_ifft)
    fshift = np.fft.fftshift(fft_img)
    mag_fft_img = 20*np.log(np.abs(fshift))
    
    img_list.append([mag_fft_img,'After Masking and FFT Image'])

    
    for img, title in img_list:
        plt.subplot(dimx, dimy, pos)
        plt.title(title)
        plt.imshow(img,cmap='gray')
        
        pos +=1
    
    plt.show()
    


if __name__=="__main__":
    processing()