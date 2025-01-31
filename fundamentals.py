import cv2
import numpy as np

img = cv2.imread('Assets/Revuelto.png', -1)
#print(img[0]) #first row of image

#img[i][j]: i é a linha e j é a coluna 
for i in range(100):
    for j in range(10):
        img[i][j] = [0, 0, 0, 0] #tornando os pixels pretos até a centésima linha e décima coluna

tag = img[140:260, 285:415] #Pegando uma parte da imagem
img[50:170, 10:140] = tag #Colando aquela parte em outro lugar da imagem, deve ser do mesmo tamanho

#print(img.shape) #shape: linhas, colunas e canais

cv2.imshow('image', img)

#Criando uma imagem a partir de um array
array_img = np.zeros(img.shape, np.uint8)
array_img[:190, :190] = [255, 255, 255, 0]

cv2.imshow('Array', array_img[:190, :190])
cv2.waitKey(0)
cv2.destroyAllWindows()