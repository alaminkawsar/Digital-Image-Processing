
from tkinter.messagebox import NO
import matplotlib.pyplot as plt
import cv2
import math
import numpy as np

def showImage(x, y, pos, img, img_title):
    plt.subplot(x,y,pos)
    plt.title(img_title)
    plt.imshow(img,cmap='gray')
    
    # plt.subplot(x,y,pos+1)
    # plt.title('RGB Histogram')
    # plt.hist(img.ravel(),256,[0,256]);

def main():
    
    #Load an RGB image from a image_path
    img_path = './Assignment/1810576130_Assignment2/flower.jpeg'
    rgb = plt.imread(img_path)
        
    x, y = 3, 2
    pos, channel = 1, 0

    grayscale = cv2.cvtColor(rgb, cv2.COLOR_RGB2GRAY)
    grayscale = np.array(grayscale)
    img1, img2, img3, img4 = np.copy(grayscale),np.copy(grayscale), np.copy(grayscale), np.copy(grayscale)
    
    #define threshold range
    T1 , T2 = 127, 200
    width, height = grayscale.shape

    for i in range(width):
        for j in range(height):
            if T1<=grayscale[i,j] and grayscale[i,j] <= T2:
                img1[i,j]=100
                img2[i,j]=100
            else:
                img1[i,j]=10
                img2[i,j]=grayscale[i,j]
    
    c, q, epsilon = 30, 2, 0.000001
    
    grayscale = cv2.cvtColor(rgb, cv2.COLOR_RGB2GRAY)
    img3 = c*np.log(1 + img3)
    img4 = c*(img4+epsilon)**q
    
    plt.figure(figsize=(5,5))
    showImage(x,y,pos,rgb,"RGB Color Image")
    showImage(x,y,pos+1,grayscale,"Gray Scale Image")
    showImage(x,y,pos+2,img1,"Change Pixel Value")
    showImage(x,y,pos+3,img2,"Change Pixel Image")
    showImage(x,y,pos+4,img2,"s = c log(1 + r)")
    showImage(x,y,pos+5,img4,"s = c ( r + epsilon )^p")
    
    plt.subplots_adjust(left=0.1,
                    bottom=0.2, 
                    right=0.9, 
                    top=0.9, 
                    wspace=1, 
                    hspace=1)
    
    plt.show()
    
if __name__ == '__main__':
	main()