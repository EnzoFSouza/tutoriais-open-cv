import cv2

img = cv2.imread('OpenCV/Assets/Revuelto.png', 1) #load image
#-1 or cv2.IMREAD_COLOR: load a color image. Transparency of image will be neglected. It's default mode
#0 or cv2.IMREAD_GRAYSCALE: load image in grayscale mode
#1 or cv2.IMREAD_UNCHANGED: load image and consider transparency 

#Resizing image
#img = cv2.resize(img, (400, 400)) #resize image to 400px by 400px
img = cv2.resize(img, (0, 0), fx = 0.5, fy = 0.5) #resize image to half its size

#Rotating image
img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

#Write an image
#This will create a file with the modified image
cv2.imwrite('newimg.png', img)


cv2.imshow('Lamborghini', img) #Display img
cv2.waitKey(0) #Wait infinite amount of time for me to press any key
cv2.destroyAllWindows()