import pytesseract
from PIL import Image
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
 

paht_img = 'extrator_texto_de_fichas/ficha.jpeg'

img = Image.open(paht_img)
imagemgray = img.convert("L")
plt.imshow(img)
plt.show()