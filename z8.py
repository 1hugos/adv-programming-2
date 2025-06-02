import cv2
import numpy as np

IMAGE_PATH = "./data/aussie_low_q.jpg"
image = cv2.imread(IMAGE_PATH)

if image is None:
    print("Błąd: nie można wczytać obrazu!")
    exit()
else:
    print("Obraz wczytano poprawnie.")

(h, w) = image.shape[:2]
center = (w // 2, h // 2)

rotated = image.copy()
for _ in range(3):
    M = cv2.getRotationMatrix2D(center, 30, 1.0)
    rotated = cv2.warpAffine(rotated, M, (w, h))

cv2.imshow("Obrót sekwencyjny: 3x30 stopni", rotated)

M_90 = cv2.getRotationMatrix2D(center, 90, 1.0)
rotated_90 = cv2.warpAffine(image, M_90, (w, h))

cv2.imshow("Obrót o 90 stopni jednorazowo", rotated_90)
cv2.waitKey(0)
cv2.destroyAllWindows()