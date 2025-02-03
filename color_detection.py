import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) #convert BGR image (The webcam image) into HSV image
    #print(hsv[width//2][height//2])
    #cv2.circle(hsv, (width//2, height//2), 3, (255, 255, 255))

    lower_blue = np.array([90, 50, 50])
    upper_blue = np.array([130, 255, 255])

    lower_orange = np.array([3, 70, 150])
    upper_orange = np.array([15, 190, 255]) #in hsv values

    #Mask:portion of an image
    mask1 = cv2.inRange(hsv, lower_blue, upper_blue)
    mask2 = cv2.inRange(hsv, lower_orange, upper_orange)

    result1 = cv2.bitwise_and(frame, frame, mask = mask1) 
    result2 = cv2.bitwise_and(frame, frame, mask = mask2) 
    #bitwise_and
    #1 1 = 1
    #1 0 = 0
    #0 1 = 0
    #0 0 = 0
    
    #cv2.imshow('mask1', mask1)
    #cv2.imshow('mask2', mask2)
    cv2.imshow('result1', result1)
    cv2.imshow('result2', result2)
    #cv2.imshow('hsv', hsv)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()