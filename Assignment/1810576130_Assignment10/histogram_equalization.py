#resources link: https://www.educative.io/answers/what-is-histogram-equalization-in-python

import numpy as np
import matplotlib.pyplot as plt
import cv2

img_path = 'low_contrast.jpg'

img = cv2.imread(img_path,0)

pos = 1
print_list = []
print_list.append([False,img,'Low Contrast Image'])
print_list.append([True,img,'Histogram of Low Contrast Image']);


ehimg = cv2.equalizeHist(img)
print_list.append([False,ehimg,'Contrast Equalization Image'])


len = int(len(print_list))
x = int((len+1)/2)

y = x
if len<=2:
    x = 2

for hist, im, title in print_list:
    if hist:
        plt.subplot(x,y,pos)
        plt.title(title)
        plt.hist(im.ravel(), 255, [0,255])
    else:
        plt.subplot(x, y, pos)
        plt.title(title)
        plt.imshow(im,cmap='gray')
    pos += 1
        
        




plt.show()
