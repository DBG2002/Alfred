import numpy as np
import matplotlib.pyplot as plt
import cv2

image_blank = np.zeros(shape=(512,512,3),dtype=np.int16)

#cv2.shape(line, rectangle etc)(image,Pt1,Pt2,color,thickness)
"""Desenhando na imagendo com esses comandos acima, onde que coordenadas 
da forma a serem traçadas de Pt1 (canto superior esquerdo) a
 Pt2 (canto inferior direito)"""

plt.imshow(image_blank) # mostra a imagem com as réguas ao lado e embaixo

#Linha Reta
# Draw a diagonal red line with thickness of 5 px
line_red = cv2.line(image_blank,(0,0),(511,511),(255,0,0),5)
plt.imshow(line_red) # mostra a imagem com as réguas ao lado e embaixo

#Retângulo - Para um retângulo, precisamos especificar as coordenadas superior esquerda e inferior direita.
#Draw a blue rectangle with a thickness of 5 px

rectangle= cv2.rectangle(image_blank,(384,0),(510,128),(0,0,255),5)
plt.imshow(rectangle)


#Texto
font = cv2.FONT_HERSHEY_SIMPLEX
text = cv2.putText(image_blank,'OpenCV',(10,500), font, 4,(255,255,255),2,cv2.LINE_AA)
plt.imshow(text)