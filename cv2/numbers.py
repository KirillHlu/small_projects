import cv2
import imutils
import numpy as np
from matplotlib import pyplot as pl

img = cv2.imread('images/car3.jpeg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

img_filter = cv2.bilateralFilter(gray, 11, 15, 15)
edges = cv2.Canny(img_filter, 30, 200)

count = cv2.findContours(edges.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
count = imutils.grab_contours(count)
count = sorted(count, key=cv2.contourArea, reverse=True)

pos = None
for c in count:
    approx = cv2.approxPolyDP(c, 10, True)
    if len(approx) == 4:
        pos = approx
        break

mask = np.zeros(gray.shape, np.uint8)
new_img = cv2.drawContours(mask, [pos], 0, 255, -1)
bitwise_img = cv2.bitwise_and(img, img, mask=mask)

pl.imshow(cv2.cvtColor(bitwise_img, cv2.COLOR_BGR2RGB))
pl.show()
