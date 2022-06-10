
import matplotlib.pyplot as plt
import cv2

def main():
    
    #Set image path
    img_path = '/home/kawsar/Desktop/Class_Resource/4th Year 1st semester/ImageProcessingLab/Open-cv/flower.jpeg'
    #print(img_path)
    
    #image read
    rgb = plt.imread(img_path)
    
    #Split loaded RGB image into grayscale, red, green, blue and binary image
    
    plt.subplot(5,2,1)
    plt.title('Red channel')
    red = rgb[:, :, 0]
    plt.imshow(red, cmap='Reds');
        
    plt.subplot(5,2,2)
    plt.title('Red Histogram')
    plt.hist(red.ravel(),256,[0,256]);
    
    plt.subplot(5,2,3)
    plt.title('Green channel')
    green = rgb[:, :, 1]
    plt.imshow(green,cmap='Greens')
    
    plt.subplot(5,2,4)
    plt.title('Green Histogram')
    plt.hist(green.ravel(),256,[0,256]);
    
    plt.subplot(5,2,5)
    plt.title('Blue channel')
    blue = rgb[:, :, 2]
    plt.imshow(blue,cmap='Blues')
    
    plt.subplot(5,2,6)
    plt.title('Blue Histogram')
    plt.hist(blue.ravel(),256,[0,256]);
    
    
    plt.subplot(5,2,7)
    plt.title('Grayscale channel')
    grayscale = cv2.cvtColor(rgb, cv2.COLOR_RGB2GRAY)
    plt.imshow(grayscale,cmap='gray')
    
    plt.subplot(5,2,8)
    plt.title('Grascale Histogram')
    plt.hist(grayscale.ravel(),256,[0,256]);
    
    plt.subplot(5,2,9)
    plt.title('Binary channel')
    th, binary_img = cv2.threshold(grayscale, 127, 255, cv2.THRESH_BINARY)
    plt.imshow(binary_img,cmap='binary')
    
    plt.subplot(5,2,10)
    plt.title('Binary Histogram')
    plt.hist(binary_img.ravel(),256,[0,256]);
    
    plt.subplots_adjust(left=0.1,
                    bottom=0.2, 
                    right=0.9, 
                    top=0.9, 
                    wspace=0.6, 
                    hspace=0.5)
    
    plt.show()
    
 
    

if __name__ == '__main__':
	main()