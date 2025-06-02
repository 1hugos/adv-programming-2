import cv2
import numpy as np

IMAGE_PATH = "./data/aussie_low_q.jpg"

image = cv2.imread(IMAGE_PATH)

if image is None:
    print("Błąd: nie można wczytać obrazu!")
    exit()
else:
    print("Obraz wczytano poprawnie.")

fragment = image[0:100, 0:100].copy()
image[100:200, 100:200] = fragment
cv2.imshow("Wklejony fragment", image)
cv2.waitKey(0)
cv2.destroyAllWindows()