
import cv2
import numpy as np

cap = cv2.VideoCapture('C:/Users/arwaa/Desktop/color maskimg/orange.mp4')

lower_bound = np.array([5, 100, 100])
upper_bound = np.array([15, 255, 255])

kernel = np.ones((5, 5), np.uint8)
display_width = 640
display_height = 480

while True:
    ret, frame = cap.read()
    if not ret:
        break


    frame = cv2.resize(frame, (display_width, display_height))

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hsv, lower_bound, upper_bound)

    mask = cv2.erode(mask, kernel, iterations=1)
    mask = cv2.dilate(mask, kernel, iterations=1)

    result = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow('Original Frame', frame)
    cv2.imshow('Result', result)

    if cv2.waitKey(30) & 0xFF == ord('s'):
        break

cap.release()
cv2.destroyAllWindows()

