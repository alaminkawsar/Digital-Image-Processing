from PIL import Image
import cv2



'''Main Image Information'''
img_path = './Assignment/1810576130_Assignment11/nature.jpeg'
image = Image.open(img_path)
print("Image Format is --> ",image.format)
#Let's check the image header
print(image,end="\n\n");


'''PNG Image Information'''
#save as png image
#image.save('Assignment/1810576130_Assignment13/from_jpg_nature.png')
img_path_png = 'Assignment/1810576130_Assignment13/from_jpg_nature.png'
png_img = Image.open(img_path_png)
print("Image Format is --> ",png_img.format)
#Let's check the image header
print(png_img,end="\n\n");


'''JPEG Image Information'''
#png_img.save('Assignment/1810576130_Assignment13/from_png_nature.jpg')
#get jpg image
img_path_jpg = 'Assignment/1810576130_Assignment13/from_png_nature.jpg'
jpg_img = Image.open(img_path_jpg)
print("Image Format is --> ",jpg_img.format)
#Let's check the image header
print(jpg_img,end="\n");


