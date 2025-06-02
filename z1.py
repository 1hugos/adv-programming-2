import cv2
import numpy as np

IMAGE_PATH = "./data/aussie_low_q.jpg"

image = cv2.imread(IMAGE_PATH)

if image is None:
    print("Błąd: nie można wczytać obrazu!")
    exit()
else:
    print("Obraz wczytano poprawnie.")

roi = image[0:100, 0:100]
cv2.imshow("Lewy górny róg", roi)
cv2.waitKey(0)
cv2.destroyAllWindows()