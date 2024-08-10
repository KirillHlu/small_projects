import cv2
import numpy as np

img = cv2.imread('images/image_10082024.jpg')

img = cv2.resize(img, (800,500))
# img = cv2.GaussianBlur(img,(111,111), 0)        #размытие
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)       #цвет

img = cv2.Canny(img, 200, 200)                    #для контуров

kernel = np.ones((5,5), np.uint8)
img = cv2.dilate(img, kernel, iterations=1)

img = cv2.erode(img, kernel, iterations=1)

cv2.imshow('Hello, world!',img)

print(img.shape)

cv2.waitKey(0)
