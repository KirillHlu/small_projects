import cv2

faces = cv2.CascadeClassifier('faces.xml')

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    if not success:
        break

    img_resized = cv2.resize(img, (640, 480))

    gray = cv2.cvtColor(img_resized, cv2.COLOR_BGR2GRAY)

    results = faces.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    for (x, y, w, h) in results:
        cv2.rectangle(img_resized, (x, y), (x + w, y + h), (0, 255, 0), thickness=3)
        cv2.putText(img_resized, 'Face', (x, y-10), cv2.FONT_HERSHEY_TRIPLEX, 1, (0, 255, 0), 1)

    cv2.imshow('Face Detection', img_resized)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
