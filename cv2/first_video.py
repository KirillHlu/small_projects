import cv2

cap = cv2.VideoCapture("C:/Users/kkhlu/OneDrive/Рабочий стол/Venice_5.mp4")
# cap.set(3, 500)
# cap.set(4, 300)

while True:
    success, img = cap.read()
    cv2.imshow('Hello, world!', img)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
