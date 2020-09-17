import cv2
import os
import numpy as np

eigenface = cv2.face.EigenFaceRecognizer_creat()
fisherface = cv2.face.FisherFaceRecognizer_creat()
lbph = cv2.face.LBPHFaceRecognizert_creat()

# Pegar as imagens para serem treinadas e organizalas
def getImagemComId():
    caminhos = [os.path.join('C:/Users/Davi/Desktop/PESSOAL/PROGRAMAS/VC/Fotos', f) for f in os.listdir('C:/Users/Davi/Desktop/PESSOAL/PROGRAMAS/VC/Fotos')]
   # print (caminhos)
    faces = []
    ids = []
    for caminhoImagem in caminhos:
        imagemFace = cv2.cvtColor(cv2.imread(caminhoImagem), cv2.COLOR_BGR2GRAY)
        id = int(os.path.split(caminhoImagem) [-1].split('.')[1])
        #print(id)
        ids.append(id)
        faces.append(imagemFace)           
      #  cv2.imshow("Face", imagemFace)
      #  cv2.waitKey(10)
    return np.array(ids), faces
    
ids, faces = getImagemComId()
print(faces)      
        
