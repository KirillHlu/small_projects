import cv2
import numpy as np

photo = np.zeros((450, 450, 3), dtype='uint8')

# photo[100:150, 200:280] = 0, 255, 0                    #высота, ширина

# cv2.rectangle(photo, (50,50), (100,100), (0,255,0), thickness=3)      #x;y,  x;y
#
# cv2.line(photo, (100,100), (150,100), (0, 255, 0), thickness=3)

# cv2.circle(photo, (photo.shape[1] // 2, photo.shape[0] // 2), 50, (0,255,0), thickness=3)

# cv2.putText(photo, 'IWDI', (photo.shape[1] // 2, photo.shape[0] // 2), cv2.FONT_HERSHEY_TRIPLEX, 1, (155,0,0), 1)

cv2.imshow('Photo', photo)
cv2.waitKey(0)
