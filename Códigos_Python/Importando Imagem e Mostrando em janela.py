import cv2
#Deve colocar o endereço da imagem e depois "/" e o nome da imagem, com o formato
img = cv2.imread('C:/Users/Davi/Pictures/mandrill_colour.png')
while True:
    cv2.imshow('mandrill',img)

    if cv2.waitKey(1) & 0xFF == 27:
        break


cv2.destroyAllWindows()

cv2.imwrite('C:/Users/Davi/Pictures/primeira_imagem.png',img)