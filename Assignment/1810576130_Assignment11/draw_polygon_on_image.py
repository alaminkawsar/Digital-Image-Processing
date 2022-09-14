from turtle import title
import numpy as np
import cv2 
import matplotlib.pyplot as plt 
import os


def processing():
    img_path = 'nature.jpeg';
    
    image = cv2.imread(img_path,0)
    
    plt.figure(figsize=(20,20))
    dimx, dimy, pos = 3, 2, 1
    img_list = []
    
    #draw circle on an image
    circle_img = cv2.circle(image.copy(),(500,300),200,(255,0,0),-1)
    rectange_img = cv2.rectangle(image.copy(),(200,300),(500,550),(255,0, 0),-1)
    
    img_list.append([image,"Main Image"])
    img_list.append([circle_img,'Circle Image'])
    img_list.append([rectange_img,'Rectangle Shape'])
    for img, title in img_list:
        plt.subplot(dimx, dimy, pos)
        plt.title(title)
        plt.imshow(img,cmap='gray')
        
        pos +=1
    
    plt.show()
    


if __name__=="__main__":
    processing()