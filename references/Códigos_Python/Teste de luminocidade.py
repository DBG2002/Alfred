import numpy as np
import cv2

camera = cv2.VideoCapture(1)


while (True):
    conectado, imagem = camera.read() #pega efeticamente a imagem da webcam
    imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY) #Transforma em cinza
    print(np.average (imagemCinza))