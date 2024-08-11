import cv2
import numpy as np

img = cv2.imread('images/image_10082024.jpg')

img = cv2.resize(img, (800,500))

new_img = np.zeros(img.shape, dtype='uint8')

img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = cv2.GaussianBlur(img, (5,5), 0)

img = cv2.Canny(img, 100, 140)

con, hir = cv2.findContours(img, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

print(con)

cv2.drawContours(new_img, con, -1, (0, 255, 0), 2)

cv2.imshow('Window', new_img)

# cv2.imwrite('photo123.jpg', new_img)

cv2.waitKey(0)
