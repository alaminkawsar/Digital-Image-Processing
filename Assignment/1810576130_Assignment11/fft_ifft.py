import numpy as np
import cv2 
import matplotlib.pyplot as plt 
import os


def processing():
    img_path = os.path.join(os.getcwd(),'1810576130_Assignment11/nature.jpeg');
    
    image = cv2.imread(img_path,0)

    fft_image = np.fft.fft2(image)
    
    shift_fft_image = np.fft.fftshift(fft_image)
    
    magnitude_image = np.log(np.abs(shift_fft_image))
    
    
    imageList = []
    imageList.append(['Main Gray Scale Image',image])
    imageList.append(['FFT Converted Images',magnitude_image])
    
    #get image
    rows, cols = image.shape
    
    crow = rows//2
    ccol = cols//2

    
    #shift_fft_image[crow-60:crow+61,ccol-60:ccol+60] = 0
    f_shift = np.fft.ifftshift(shift_fft_image)
    img_back = np.fft.ifft2(f_shift)
    img_back = np.log(np.abs(img_back))
    
    imageList.append(['IFF Converted Images',img_back])
    
    
    pos = 1
    for title, img in imageList:
        plt.subplot(22*10+pos)
        plt.imshow(img,cmap='gray')
        plt.title(title)
        plt.xticks([])
        plt.yticks([])
        pos += 1

    plt.show()
    
    print(img_path)



if __name__=="__main__":
    processing()