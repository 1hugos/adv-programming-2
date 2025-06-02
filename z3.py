import cv2
import numpy as np

IMAGE_PATH = "./data/aussie_low_q.jpg"
image = cv2.imread(IMAGE_PATH)

if image is None:
    print("Błąd: nie można wczytać obrazu!")
    exit()
else:
    print("Obraz wczytano poprawnie.")

cv2.imshow("Oryginalny obraz", image)

(h, w) = image.shape[:2]

M = cv2.getRotationMatrix2D((0, 0), 30, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))

cv2.imshow("Obrót o 30 stopni względem narożnika", rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()