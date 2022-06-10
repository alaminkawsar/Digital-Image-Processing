import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
img_path = './Assignment/1810576130_Assignnment3/flower.jpeg'
img = plt.imread(img_path)
img = np.array(img)

def plot_img(x, y, pos, img, img_title):
    plt.subplot(x,y,pos)
    plt.title(img_title)
    plt.imshow(img,cmap='gray')
    
    # plt.subplot(x,y,pos+1)
    # plt.title('RGB Histogram')
    # plt.hist()



def main():
    x, y = 4, 2
    pos, channel = 1, 0
    
    img_path = './Histogram-opencv-matplotlib/flower.jpeg'
    img = cv.imread(img_path,0)
    plot_img(x,y,pos,img,"GRAY")
    
    plt.subplot(x,y,pos+1)
    image= np.copy(np.array(img));
    plt.hist(image.ravel(),256,[0,256]);
    
    plt.subplot(x,y,pos+2)
    dummie_data = np.random.randint(0, 256, (100,100))

    values, count = np.unique(dummie_data, return_counts=True)

    plt.figure(figsize=(10,6))
    plt.bar([x for x in range(0,256)], count, width=0.9)
    
    plt.show()
    
if __name__ == '__main__':
    main()