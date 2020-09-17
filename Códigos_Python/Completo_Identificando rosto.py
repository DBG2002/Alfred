import numpy as np
import cv2
import matplotlib.pyplot as plt


#Loading the image to be tested
test_image = cv2.imread('C:/Users/Davi/Pictures/baby1.jpg')



#Converting to grayscale
test_image_gray = cv2.cvtColor(test_image, cv2.COLOR_BGR2GRAY)



# Displaying the grayscale image
plt.imshow(test_image_gray, cmap='gray')


# Como sabemos que o OpenCV carrega uma imagem no formato BGR, precisamos convertê-la para o formato RBG para poder exibir suas cores verdadeiras. Vamos escrever uma pequena função para isso.
def convertToRGB(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)



#Calssificador de rosto do Haar (Somente da Face frontal, porém ele tem dos olhos, boca e etc)
haar_cascade_face = cv2.CascadeClassifier('C:/Users/Davi/Desktop/PESSOAL/PROGRAMAS/VC/haarcascade/haarcascade_frontalface_default.xml') #Calssificador de rosto do Haar
faces_rects = haar_cascade_face.detectMultiScale(test_image_gray, scaleFactor = 1.2, minNeighbors = 5);

# Let us print the no. of faces found
print('Faces found: ', len(faces_rects))


"""Nosso próximo passo é fazer um loop em todas as coordenadas que ele retornou
 e desenhar retângulos ao redor delas usando Open CV. 
 Estaremos desenhando um retângulo verde com espessura de 2"""
for (x,y,w,h) in faces_rects:
     cv2.rectangle(test_image, (x, y), (x+w, y+h), (0, 255, 0), 2)  
     
     
     
#convert image to RGB and show image
plt.imshow(convertToRGB(test_image))


# Detecção de rosto com função generalizada
def detect_faces(cascade, test_image, scaleFactor = 1.2):
    # create a copy of the image to prevent any changes to the original one.
    image_copy = test_image.copy()

    #convert the test image to gray scale as opencv face detector expects gray images
    gray_image = cv2.cvtColor(image_copy, cv2.COLOR_BGR2GRAY)

    # Applying the haar classifier to detect faces
    faces_rect = cascade.detectMultiScale(gray_image, scaleFactor=scaleFactor, minNeighbors=5)

    for (x, y, w, h) in faces_rect:
        cv2.rectangle(image_copy, (x, y), (x+w, y+h), (0, 255, 0), 2)

    return image_copy  



 #loading image
test_image2 = cv2.imread('C:/Users/Davi/Pictures/baby1.jpg')

 # Converting to grayscale
test_image_gray = cv2.cvtColor(test_image, cv2.COLOR_BGR2GRAY)

  # Displaying grayscale image
plt.imshow(test_image_gray, cmap='gray')


#call the function to detect faces
faces = detect_faces(haar_cascade_face, test_image2)

 #convert to RGB and display image
plt.imshow(convertToRGB(faces))