#Importação dos Módulos
import numpy as np
import cv2
import matplotlib.pyplot as plt





# Definição das funções

    # Como sabemos que o OpenCV carrega uma imagem no formato BGR, precisamos convertê-la para o formato RBG para poder exibir suas cores verdadeiras. Vamos escrever uma pequena função para isso.
def convertToRGB(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)


    # Calssificador de rosto do Haar (Somente da Face frontal, porém ele tem dos olhos, boca e etc)
haar_cascade_face = cv2.CascadeClassifier('C:/Users/Davi/Desktop/PESSOAL/PROGRAMAS/VC/haarcascade/haarcascade_frontalface_default.xml') #Calssificador de rosto do Haar

 
    # Detecção de rosto com função generalizada
def detect_faces(cascade, test_image, scaleFactor = 1.1):
    # create a copy of the image to prevent any changes to the original one.
    image_copy = test_image.copy()

    #convert the test image to gray scale as opencv face detector expects gray images
    gray_image = cv2.cvtColor(image_copy, cv2.COLOR_BGR2GRAY)

    # Applying the haar classifier to detect faces
    faces_rect = cascade.detectMultiScale(gray_image, scaleFactor=scaleFactor, minNeighbors=5)
    

    for (x, y, w, h) in faces_rect:
        cv2.rectangle(image_copy, (x, y), (x+w, y+h), (0, 255, 0), 4)

    return image_copy  





# Programa Principal
    
    # Carregar a imagem
test_image = cv2.imread('C:/Users/Davi/Pictures/baby2.jpg')


    # Converter para a escala em cinza
test_image_gray = cv2.cvtColor(test_image, cv2.COLOR_BGR2GRAY)


    # Exibindo imagem em tons de cinza
plt.imshow(test_image_gray, cmap='gray')


    # chamar a função para detectar rostos 
faces = detect_faces(haar_cascade_face, test_image)


    # Converter para Red Green Blue e mostrar
plt.imshow(convertToRGB(faces))


