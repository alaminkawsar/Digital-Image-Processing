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
    # plt.hist(img.ravel(),256,[0,256])



def main():
    x, y = 4, 2
    pos, channel = 1, 0

    #define six kernal
    Vertical_kernel = np.array([[1,0,-1],
                                [1,0,-1],
                                [1,0,-1]]) #kernal size 3x3
    
    Horizontal_kernel = np.array([[1,1,1],
                                  [0,0,0],
                                  [-1,-1,-1]]) #kernal size 3x3
    
    Sobel_vertical_kernel = np.array([[1,0,-1],
                                      [2,0,-2],
                                      [1,0,-1]]) #kernal size 3x3
    
    Scharr_vertical_kernel = np.array([[3,0,-3],
                                       [10,0,-10],
                                       [3,0,-3]]) #kernal size 3x3
    my_kernel = np.array([[1,0,-2,1],
                          [1,-1,1,-1],
                          [1,0,-2,1],
                          [-3,1,-2,-1],
                          [0,3,1,2]]) # kernal size 5x5
    Gaussian_kernel = np.array([[-1,4,-7,4,-1],
                                [-4,16,-5,16,4],
                                [-3,26,-41,26,-7],
                                [-4,16,-26,-16,4],
                                [1,-4,7,-4,1]])/10 # kernal size 5x5

    print("Vertical_kernel{}".format(Vertical_kernel))
    print("Horizontal_kernel{}".format(Horizontal_kernel))
    print("Sobel_vertical_kernel{}".format(Sobel_vertical_kernel))
    print("Scharr_vertical_kernel{}".format(Scharr_vertical_kernel))
    print("my_kernel{}".format(Gaussian_kernel))
    print("Gaussian_kernel{}".format(my_kernel))

    #Neighborhood Processing
    '''	Convert the RGB image into grayscale and binary image.	'''
    grayscale = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
    Vertical_kernel_output = cv.filter2D(grayscale, -1, Vertical_kernel)
    Horizontal_kernel_output = cv.filter2D(grayscale, -1, Horizontal_kernel)
    Sobel_kernel_output = cv.filter2D(grayscale, -1, Sobel_vertical_kernel)
    Scharr_kernel_output = cv.filter2D(grayscale, -1, Scharr_vertical_kernel)
    Gaussian_kernel_output = cv.filter2D(grayscale, -1, Gaussian_kernel)
    my_kernel_output = cv.filter2D(grayscale, -1, my_kernel)


    plot_img(x,y,pos,img,"RGB Color Image")
    plot_img(x,y,pos+1,grayscale,"Gray Scale Image")
    plot_img(x,y,pos+2,Vertical_kernel_output,"Vertical Kernel Effect output")
    plot_img(x,y,pos+3,Horizontal_kernel_output,"Horizontal Kernel Effect output")
    plot_img(x,y,pos+4,Sobel_kernel_output,"Sobel_vertical_kernel output")
    plot_img(x,y,pos+5,Scharr_kernel_output,"Scharr_vertical_kernel output")
    plot_img(x,y,pos+6,Gaussian_kernel_output,"Gaussian_kernel output")
    plot_img(x,y,pos+7,my_kernel_output,"my_kernel")
    
    plt.subplots_adjust(left=0.1,
                    bottom=0.01, 
                    right=1, 
                    top=0.95, 
                    wspace=0.0, 
                    hspace=0.3)
    
    plt.show()


if __name__ == '__main__':
    main()