#Import cv2 nump and matplotlib
import cv2
import numpy as np
from matplotlib import pyplot as plt

#imported ATU jpeg using cv2
img = cv2.imread('ATU.jpg',)

#converted the image to grayscale
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#3x3 blur
blur3 = cv2.GaussianBlur(img,(3, 3),0)
#13x13 blur
blur13 = cv2.GaussianBlur(img,(13, 13),0)

sobelX = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5) # x dir
sobelY = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5) # y dir

#Sobel X and Y together
sobelXY = cv2.Sobel(img,cv2.CV_64F,1,1,ksize=5) #x + y dir

#Canny edge detection canny = cv2.Canny(imgIn,cannyThreshold,cannyParam2)
#cannyParam2 should be 2-3 times the magnitude of cannyThreshold
canny = cv2.Canny(img,100,200)

#Plotting the first coloured image
plt.subplot(2, 3, 1),plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB), cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])

#Plotting the gray scaled image
plt.subplot(2, 3, 2),plt.imshow(gray_image, cmap = 'gray')
plt.title('GrayScale'), plt.xticks([]), plt.yticks([])

#Plotting Horizontal sobel
plt.subplot(2, 3, 3),plt.imshow(sobelX, cmap = 'gray')
plt.title('sobelX'), plt.xticks([]), plt.yticks([])

#Plotting Vertical sobel
plt.subplot(2, 3, 4),plt.imshow(sobelY, cmap = 'gray')
plt.title('sobelY'), plt.xticks([]), plt.yticks([])

#Plotting sobel sum
plt.subplot(2, 3, 5),plt.imshow(sobelXY, cmap = 'gray')
plt.title('sobel sum'), plt.xticks([]), plt.yticks([])

#Plotting Canny
plt.subplot(2, 3, 6),plt.imshow(canny, cmap = 'gray')
plt.title('Canny Edge Image'), plt.xticks([]), plt.yticks([])

#displaying the image
plt.show()

cv2.waitKey(0)  
cv2.destroyAllWindows()