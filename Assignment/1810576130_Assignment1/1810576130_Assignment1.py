
import matplotlib.pyplot as plt
import cv2


def main():
    
    #Load an RGB image from a image_path
    img_path = './1810576130_Assignment1/flower.jpeg'
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
    plt.imshow(grayscale, cmap='gray')
    
    plt.subplot(x,y,pos+1)
    plt.title('Grascale Histogram')
    plt.hist(grayscale.ravel(),256,[0,256]);

    # pos += 2
    # plt.subplot(x,y,pos)
    # plt.title('Binary channel')
    # th, binary_img = cv2.threshold(grayscale, 127, 255, cv2.THRESH_BINARY)
    # plt.imshow(binary_img, cmap='binary')
    
    # plt.subplot(x,y,pos+1)
    # plt.title('Binary Histogram')
    # plt.hist(binary_img.ravel(),256,[0,256]);
    
    # plt.subplots_adjust(left=0.1,
    #                 bottom=0.2, 
    #                 right=0.9, 
    #                 top=0.9, 
    #                 wspace=1, 
                    hspace=1)
    
    plt.show()
    
if __name__ == '__main__':
	main()