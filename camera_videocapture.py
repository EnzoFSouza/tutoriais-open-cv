import numpy as np
import cv2

cap = cv2.VideoCapture(0) #use webcam camera

while True:
    ret, frame = cap.read()
    width = int(cap.get(3)) #give the width of the frame
    height = int(cap.get(4)) #give the height of the frame

    image = np.zeros(frame.shape, np.uint8) #unsigned integer 8 bits
    smaller_frame = cv2.resize(frame, (0,0), fx = 0.5, fy = 0.5)
    image[:height//2, :width//2] = cv2.rotate(smaller_frame, cv2.ROTATE_180)
    image[height//2:, :width//2] = smaller_frame
    image[:height//2, width//2:] = cv2.rotate(smaller_frame, cv2.ROTATE_180)
    image[height//2:, width//2:] = smaller_frame

    cv2.imshow('Webcam', image)

    if cv2.waitKey(1) == ord('q'): #the function returns the ordinal value of the key pressed
        #wait up to 1 milissecond
        #if we press a key within 1 milissecond, the function is going to return the ordinal value
        break

cap.release()
cv2.destroyAllWindows()