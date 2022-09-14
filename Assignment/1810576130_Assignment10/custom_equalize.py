# https://levelup.gitconnected.com/introduction-to-histogram-equalization-for-digital-image-enhancement-420696db9e43

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import cv2 

#from Abir
#tutorial from : https://www.tutorialspoint.com/dip/histogram_equalization.htm
def get_custom_equalize_Hist(img):
    hist,bins = np.histogram(img,256,[0,256])
    cdf = hist.cumsum()
    m, n = img.shape
    new_img = img.copy()
    for i in range(m):
        for j in range(n):
            new_img[i,j] = np.round((cdf[img[i,j]] - cdf.min())/(m*n-cdf.min()) * ((1<<8) -1))
    
    return new_img
    
    
img = cv2.imread('man.png', 0)

plt.figure(figsize=(20,20))

dimx, dimy , pos = 3, 2, 1

img_list = []
img_list.append([True, img,'Main Image'])
img_list.append([False, img,'Histogram of Main Image'])

ehimg = cv2.equalizeHist(img)
img_list.append([True, ehimg,'Equalize Histogram Image'])
img_list.append([False, ehimg,'Equalize Histogram'])

custom_ehimg = get_custom_equalize_Hist(img)
img_list.append([True, custom_ehimg,'Custom Equalize Histogram Image'])
img_list.append([False, custom_ehimg,'Custom Equalize Histogram'])

for type, image, title in img_list:
    plt.subplot(dimx, dimy, pos)
    plt.title(title)

    if type==True:
        plt.imshow(image,cmap='gray')
    else:
        plt.hist(image.ravel(),256,[0,256])
    pos +=1

# plt.title('Custom Histogram')
# plt.subplot(dimx,dimy,pos)
# plt.bar(pixels,hist,width=1.1)

plt.show()