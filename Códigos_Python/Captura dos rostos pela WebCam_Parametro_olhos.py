import cv2
import numpy as np
 
classificador = cv2.CascadeClassifier('C:/Users/Davi/Desktop/PESSOAL/PROGRAMAS/VC/haarcascade/haarcascade_frontalface_default.xml') # Parametros que definem um rosto
classificadorOlho = cv2.CascadeClassifier ('C:/Users/Davi/Desktop/PESSOAL/PROGRAMAS/VC/haarcascade/haarcascade_eye.xml') # Parametros que definem um olho
camera = cv2.VideoCapture(0)  #instancia o uso da webcam
amostra = 1 # Base para poder acompanhar o numero de amostras
numeroAmostras = 25 #Número total de amostras
id = input('Digite seu identificador: ') # Identificador de cada pessoa
largura, altura = 220, 220 # Define o tamanho da imagem
print("Capturando as faces....")

while (True): # Fazer com que o processo seja em loop
    conectado, imagem = camera.read() #pega efeticamente a imagem da webcam
    imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY) #Transforma em cinza para a detecção do rosto, pois a leitura do haar é em cinza
    facesDetectadas = classificador.detectMultiScale(imagemCinza, # Detecta todas as faces da imagem e defini a scala e tamanho minimo
                                                     scaleFactor=1.5,
                                                     minSize=(150, 150))
 
    # Desenha um retângulo nas faces detectadas
    for (x, y, l, a) in facesDetectadas:
        cv2.rectangle(imagem, (x, y), (x+l, y+a), (0, 0, 255), 2)
        regiao  = imagem[y:y +a, x:x + l] # Define a regiao do rosto
        regiaoCinzaOlho = cv2.cvtColor(regiao, cv2.COLOR_BGR2GRAY) # Transforma em cinza os olhos
        olhosDetectados = classificadorOlho.detectMultiScale(regiaoCinzaOlho) # Detecta os olhos, medida de segurança para a foto pegar um rosto
        for (ox, oy, ol, oa) in olhosDetectados: # Desenha um retângulo nos olhos detectados
            cv2.rectangle(regiao, (ox, oy), (ox +ol, oy +oa), (0,255,0),2)
            
        
            if cv2.waitKey(1) & 0xFF == ord('p'): # Tecla para tirar a foto
                if np.average (imagemCinza) > 110: # Parametro de segurança, se tiver luz suficiente na camera = 110
                    imagemFace = cv2.resize(imagemCinza[y:y + a, x:x + l], (largura, altura)) # Redimensiona o tamanho da foto
                    cv2.imwrite("C:/Users/Davi/Desktop/PESSOAL/PROGRAMAS/VC/Fotos/pessoa." + str(id) + "." + str(amostra) + ".jpg", imagemFace) # Local onde será salvo a foto
                    print("[Foto " + str(amostra) + " capturada com sucesso]")
                    amostra += 1 # Define a quantidade de amostras que estão sendo capturadas
    cv2.imshow("Face", imagem) #mostra a imagem captura na janela
    cv2.waitKey(1)
    if (amostra >= numeroAmostras + 1): # Controla a quantidade de amostras total
            break
          

print("Faces capturadas com sucesso")

camera.release() #dispensa o uso da webcam
cv2.destroyAllWindows() #fecha todas a janelas 


