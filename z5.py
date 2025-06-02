import cv2
import numpy as np
import imutils

IMAGE_PATH = "./data/aussie_low_q.jpg"
image = cv2.imread(IMAGE_PATH)

if image is None:
    print("Błąd: nie można wczytać obrazu!")
    exit()
else:
    print("Obraz wczytano poprawnie.")

cv2.imshow("Oryginalny obraz", image)

rotated = imutils.rotate(image, 180)

cv2.imshow("Obrót o 180 stopni (imutils)", rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()