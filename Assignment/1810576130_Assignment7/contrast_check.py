import numpy as np
import cv2
import matplotlib.pyplot as plt
import os

img_path = './flower.jpeg'
#print(img_path)
x, y, pos = 4, 2, 1

plt_list = []
rgb = plt.imread(img_path)
grayscale = cv2.cvtColor(rgb,cv2.COLOR_RGB2GRAY)
temp = (grayscale-50)%200

left = temp
right = temp + 50
middle = (temp %150)+50

plt_list.append([grayscale, 'Main Image '])
plt_list.append([left,'Left '])
plt_list.append([right, 'Right '])
plt_list.append([middle,'Middle '])

for item in plt_list:
    plt.subplot(x,y,pos)
    plt.title(item[1])
    plt.imshow(item[0],cmap='gray')

    plt.subplot(x,y,pos+1)
    plt.title(item[1]+'Histogram')
    histr = cv2.calcHist([item[0]],[0],None,[256],[0,256])
    plt.plot(histr,color = 'blue')
    plt.xlim([0,256])
    
    pos += 2
    
plt.show()