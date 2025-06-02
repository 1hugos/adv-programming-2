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

rotated = imutils.rotate_bound(image, -33)

cv2.imshow("Obrót o -33 stopnie bez przycinania", rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()