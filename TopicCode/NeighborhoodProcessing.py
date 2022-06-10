'''	
	------------------
	Neighborhood processing.
	------------------
	Sangeeta Biswas
	Associate Professor
	Dept. of Computer Science & Engineering
	University of Rajshahi
	Rajshahi, Bangladesh
	
	7.6.2022
'''

import matplotlib.pyplot as plt
import cv2
import numpy as np

def main():
	'''	Load an RGB image.	'''
	img_path = './TopicCode/flower.jpeg'
	rgb = plt.imread(img_path)
	print(rgb.shape)
		
	'''	Convert the RGB image into grayscale and binary image.	'''
	grayscale = cv2.cvtColor(rgb, cv2.COLOR_RGB2GRAY)
	print(grayscale.shape)
	
	'''	Prepare kernels/filters/masks.	'''
	kernel1 = np.ones((3, 3), dtype = np.float32) * 2 / 9
	print('Kernel1: {}'.format(kernel1))	
	kernel2 = np.array([[0, -1, 0], [-1, 4, -1], [0, -1, 0]])
	print('Kernel2: {}'.format(kernel2))
	
	'''	Neighborhood processing. '''
	processed_img1 = cv2.filter2D(grayscale, -1, kernel1)
	processed_img2 = cv2.filter2D(grayscale, -1, kernel2)
		
	'''	Plot images. '''
	img_set = [rgb, grayscale, processed_img1, processed_img2]
	title_set = ['RGB', 'Grayscale', 'Kernel1', 'Kernel2']
	plot_img(img_set, title_set)

def plot_img(img_set, title_set):
	n = len(img_set)
	plt.figure(figsize = (20, 20))
	for i in range(n):
		img = img_set[i]
		ch = len(img.shape)
	
		plt.subplot(2, 2, i + 1)
		if (ch == 3):
			plt.imshow(img_set[i])
		else:
			plt.imshow(img_set[i], cmap = 'gray')
		plt.title(title_set[i])
	plt.show()		
	
if __name__ == '__main__':
	main()