import matplotlib.pyplot as plt
import cv2
import numpy as np



def main():
    
    #Load an RGB image from a image_path
    img_path = '/home/kawsar/Desktop/Class_Resource/4th Year 1st semester/ImageProcessingLab/Assignment/1810576130_Assignment5/flower.jpeg'
    #print(img_path)
    rgb = plt.imread(img_path)
    #print(rgb)
    
    #Split loaded RGB image into grayscale, red, green, blue and binary image
    
    x, y = 5, 2
    pos, channel = 1, 0
    
    plt.figure(figsize=(20,20))
    
    
    plt.subplot(x,y,pos)
    plt.title('Grayscale channel')
    grayscale = cv2.cvtColor(rgb, cv2.COLOR_RGB2GRAY)
    grayscale = cv2.resize(grayscale, (680,580))
    plt.imshow(grayscale, cmap='gray')

    
    w, h = grayscale.shape
    
    
    mat = np.zeros((8,w,h),dtype=int)
    bitset = [1,2,4,8,16,32,64,128]    

    for k in range(8):
        for i in range(w):
            for j in range(h):
                mat[k][i][j] = grayscale[i][j] & bitset[k]
    k = 7
     
    for pos in range(2,10):
        plt.subplot(x,y,pos)
        plt.title(str(k+1)+ 'Bits')
        plt.imshow(mat[k], cmap='gray')
        k -= 1
        
    restore_img = np.zeros((w,h),dtype=int)
    
    for k in range(8):
        for i in range(w):
            for j in range(h):
                restore_img[i][j] += mat[k][i][j]
                
    plt.subplot(x,y,10)
    plt.title('Restored Image')
    plt.imshow(restore_img,cmap='gray')
    
    
    plt.subplots_adjust(left=0.1,
                    bottom=0.2, 
                    right=0.9, 
                    top=0.9, 
                    wspace=1, 
                    hspace=1)
    
    plt.show()
    
if __name__ == '__main__':
	main()