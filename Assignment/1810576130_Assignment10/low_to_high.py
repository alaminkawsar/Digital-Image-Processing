import numpy as np
import matplotlib.pyplot as plt
import cv2

img_path = 'nature_sea.jpeg'

img = cv2.imread(img_path,0)

x, y , pos = 1, 2, 1
print_list = []
print_list.append([False,img,'Main Image'])
print_list.append([True,img,'Histogram of Main Image']);


# ehimg = cv2.equalizeHist(img)
# print_list.append([False,ehimg,'Histogram Equalization Image'])
# print_list.append([True, ehimg, 'Histogram of Histogram Equalization'])


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

plt.savefig('./low_contrast.png')