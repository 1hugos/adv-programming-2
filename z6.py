import cv2
import numpy as np
from matplotlib import pyplot as plt

IMAGE_PATH = "./data/aussie_low_q.jpg"

image = cv2.imread(IMAGE_PATH)

if image is None:
    print("Błąd: nie można wczytać obrazu!")
    exit()
else:
    print("Obraz wczytano poprawnie.")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
brighter = cv2.add(gray, 50)
hist = cv2.calcHist([brighter], [0], None, [256], [0, 256])
otsu_val, _ = cv2.threshold(brighter, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

plt.plot(hist)
plt.axvline(x=otsu_val, color='r', linestyle='--')
plt.title("Histogram jasności z progiem Otsu")
plt.show()