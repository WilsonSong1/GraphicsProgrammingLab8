#Import cv2 nump and matplotlib
import cv2
import numpy as np
from matplotlib import pyplot as plt

#imported ATU jpeg using cv2
img = cv2.imread('ATU.jpg',)

#converted the image to grayscale
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

imgOut = cv2.GaussianBlur(img,(13, 13),0)

#Plotting the first coloured image
plt.subplot(2, 2, 1),plt.imshow(cv2.cvtColor(imgOut, cv2.COLOR_BGR2RGB), cmap = 'gray')
plt.title('1'), plt.xticks([]), plt.yticks([])

#Plotting the gray scaled image
plt.subplot(2, 2, 2),plt.imshow(gray_image, cmap = 'gray')
plt.title('2'), plt.xticks([]), plt.yticks([])

#displaying the image
plt.show()

cv2.waitKey(0)  
cv2.destroyAllWindows()