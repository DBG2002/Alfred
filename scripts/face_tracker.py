import cv2

class FaceTracker(object):
    """
    docstring
    """
    
    def __init__(self):
        """
        Face Tracker constructor
        """
        self.face_cascade = cv2.CascadeClassifier('../references/haarcascade/haarcascade_frontalface_default.xml')
        

    def begin(self):
        """
        docstring
        """
        webcam = cv2.VideoCapture(0)  #instancia o uso da webcam
        
        while True:
            s, imagem = webcam.read() #pega efeticamente a imagem da webcam
            imagem = cv2.flip(imagem,180) #espelha a imagem
        
            faces = self.face_cascade.detectMultiScale(
                imagem,
                minNeighbors=5,
                minSize=(30, 30),
            maxSize=(200,200)
            )
        
            # Desenha um retângulo nas faces detectadas
            for (x, y, l, a) in faces:
                cv2.rectangle(imagem, (x, y), (x+l, y+a), (0, 255, 0), 2)
                # print(x,y) 
                # print ("Altura Y (height): %d pixels" % (imagem.shape[0]))
                # print ("Largura X (width): %d pixels" % (imagem.shape[1]))
                # print ("Canais (channels): %d"      % (imagem.shape[2]))
                font = cv2.FONT_HERSHEY_SIMPLEX
                if x < 160: # Detectar se o rosto está no quadro esquerdo
                    cv2.putText(imagem,'esquerda',(10,400), font, 3,(255,255,255),2,cv2.LINE_AA)
                elif x > 320: # Detectar se o rosto está no quadro direito
                    cv2.putText(imagem,'direita',(10,400), font, 3,(255,255,255),2,cv2.LINE_AA)
                if y < 120: # Detectar se o rosto está no quadro superior
                    cv2.putText(imagem,'Subiu',(30,200), font, 3,(255,255,255),2,cv2.LINE_AA)
                elif y > 240: # Detectar se o rosto está no quadro inferior
                    cv2.putText(imagem,'Desceu',(30,200), font, 3,(255,255,255),2,cv2.LINE_AA)
            cv2.imshow('Video', imagem) #mostra a imagem captura na janela
                    
            
            #o trecho seguinte é apenas para parar o código e fechar a janela
            if cv2.waitKey(1) & 0xFF == 27:
                break
        
        webcam.release() #dispensa o uso da webcam
        cv2.destroyAllWindows() #fecha todas a janelas abertas
