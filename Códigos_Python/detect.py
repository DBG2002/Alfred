import cv2

captura = cv2.VideoCapture(1)

while(1):
    ret, frame = captura.read()
    cv2.imshow("teste3.jpg", frame)
    break
        
 
captura.release()
cv2.destroyAllWindows()

