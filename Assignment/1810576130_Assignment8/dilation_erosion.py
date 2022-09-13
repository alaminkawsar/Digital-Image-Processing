import numpy as np
import cv2 
import matplotlib.pyplot as plt

img_path = '/home/kawsar/Desktop/Class_Resource/4th year 1st semester/4181- Digital Image Processing/ImageProcessingLab/Assignment/1810576130_Assignment8/tree.jpg'
img = plt.imread(img_path)
_, img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
# Taking a matrix of size 5 as the kernel
kernel1 = np.ones((5, 5), np.uint8)
kernel2 = np.ones((3,3), np.uint8)
kernel3 = np.ones((7,7), np.uint8)

x, y, pos = 2, 3, 1

#erosion Image
img_erosion1 = cv2.erode(img, kernel1, iterations=1)
img_erosion2 = cv2.erode(img, kernel2, iterations=1)
img_erosion3 = cv2.erode(img, kernel3, iterations=1)

#dilation Image
img_dilation1 = cv2.dilate(img, kernel1, iterations=1)
img_dilation2 = cv2.dilate(img, kernel2, iterations=1)
img_dilation3 = cv2.dilate(img, kernel3, iterations=1)


#closing_image
closing_img1 = cv2.dilate(img_erosion1, kernel1, iterations=1)
closing_img2 = cv2.dilate(img_erosion2, kernel1, iterations=1)
closing_img3 = cv2.dilate(img_erosion3, kernel1, iterations=1)


#opening image
opening_img1 = cv2.erode(img_dilation1, kernel1, iterations=1)
opening_img2 = cv2.erode(img_dilation2, kernel1, iterations=1)
opening_img3 = cv2.erode(img_dilation3, kernel1, iterations=1)

image_list = []
title_list = ['Main Image','Erosion Image','Dilation Image','Closing Image','Openning Imgage']

image_list.append(img)
image_list.append(img_erosion1)
image_list.append(img_dilation1)
image_list.append(closing_img1)
image_list.append(opening_img1)

# plt.figure(figsize=(20,20))
# plt.subplot(x, y, pos)
# plt.imshow(img)

for item in image_list:
    plt.subplot(x, y, pos)
    plt.title(title_list[pos-1])
    plt.imshow(item,cmap='gray')
    pos += 1

plt.show()
