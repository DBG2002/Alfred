
import cv2
import numpy as np
import matplotlib.pyplot as plt

imagem = 'C:/Users/Davi/Pictures/mandrill_colour.png'

img_raw = cv2.imread(imagem)
type(img_raw)
np.ndarray

img_raw.shape
(1300, 1950, 3)

plt.imshow(img_raw)
img = cv2.cvtColor(img_raw, cv2.COLOR_BGR2RGB)
plt.imshow(img)