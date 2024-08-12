import cv2

img = cv2.imread('images/faces1.jpg')
img = cv2.resize(img, (800,500))
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = cv2.CascadeClassifier('faces.xml')

results = faces.detectMultiScale(gray, scaleFactor=2, minNeighbors=3)

for (x,y, w, h) in results:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), thickness=3)

cv2.imshow('IWDI', img)
cv2.waitKey(0)
