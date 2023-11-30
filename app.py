
import pytesseract
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt


filename = "image.jpg"

# img = cv2.imread(filename)
# gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 

array_image = np.array(Image.open(filename))
imgplot = plt.imread(array_image)

plt.imshow(imgplot)