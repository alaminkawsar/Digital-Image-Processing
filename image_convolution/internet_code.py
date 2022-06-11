import numpy as np
from PIL import Image, ImageOps
import matplotlib.pyplot as plt
import cv2 as cv

def get_padding_width_per_side(kernel_size: int) -> int:
    # Simple integer division
    return kernel_size // 2

def add_padding_to_image(img: np.array, padding_width: int) -> np.array:
    # Array of zeros of shape (img + padding_width)
    img_with_padding = np.zeros(shape=(
        img.shape[0] + padding_width * 2,  # Multiply with two because we need padding on all sides
        img.shape[1] + padding_width * 2
    ))
    
    # Change the inner elements
    # For example, if img.shape = (224, 224), and img_with_padding.shape = (226, 226)
    # keep the pixel wide padding on all sides, but change the other values to be the same as img
    img_with_padding[padding_width:-padding_width, padding_width:-padding_width] = img
    
    return img_with_padding


def convolve(img: np.array, kernel: np.array) -> np.array:
    # Assuming a rectangular image
    tgt_size = calculate_target_size(
        img_size=img.shape[0],
        kernel_size=kernel.shape[0]
    )
    # To simplify things
    k = kernel.shape[0]
    
    # 2D array of zeros
    convolved_img = np.zeros(shape=(tgt_size, tgt_size))
    
    # Iterate over the rows
    for i in range(tgt_size):
        # Iterate over the columns
        for j in range(tgt_size):
            # img[i, j] = individual pixel value
            # Get the current matrix
            mat = img[i:i+k, j:j+k]
            
            # Apply the convolution - element-wise multiplication and summation of the result
            # Store the result to i-th row and j-th column of our convolved_img array
            convolved_img[i, j] = np.sum(np.multiply(mat, kernel))
            
    return convolved_img

def calculate_target_size(img_size: int, kernel_size: int) -> int:
    num_pixels = 0
    
    # From 0 up to img size (if img size = 224, then up to 223)
    for i in range(img_size):
        # Add the kernel size (let's say 3) to the current i
        added = i + kernel_size
        # It must be lower than the image size
        if added <= img_size:
            # Increment if so
            num_pixels += 1
            
    return num_pixels

def plot_image(img: np.array):
    plt.figure(figsize=(6, 6))
    plt.imshow(img, cmap='gray');
    
def plot_two_images(img1, img2):
    _, ax = plt.subplots(1, 2, figsize=(12, 6))
    ax[0].imshow(img1, cmap='gray')
    ax[1].imshow(img2, cmap='gray');

def main():
    img = cv.imread('/home/kawsar/Desktop/Class_Resource/4th Year 1st semester/ImageProcessingLab/image_convolution/flower.jpeg',0)
    resized_img = cv.resize(img,(224,224),interpolation = cv.INTER_AREA)
    #plot_image(resized_img)
    
    sharpen = np.array([
        [0, -1, 0],
        [-1, 5, -1],
        [0, -1, 0]
    ])

    blur = np.array([
        [0.0625, 0.125, 0.0625],
        [0.125,  0.25,  0.125],
        [0.0625, 0.125, 0.0625]
    ])

    outline = np.array([
        [-1, -1, -1],
        [-1,  8, -1],
        [-1, -1, -1]
    ])
    img = resized_img
    
    img_with_padding_3x3 = add_padding_to_image(
        img=np.array(img), 
        padding_width=1
    )

    print(img_with_padding_3x3.shape)
    #plot_image(img_with_padding_3x3)
    
    img_sharpened = convolve(img=img_with_padding_3x3, kernel=sharpen)
    conv_img = cv.filter2D(img,-1,sharpen)
    print(img_sharpened,"\n\n\n",conv_img)
    
    plot_two_images(img_sharpened,conv_img)
    
    
    
    plt.show()

if __name__ == '__main__':
    main()