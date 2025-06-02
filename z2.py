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

roi = image[h // 2:h, :]
cv2.imshow("Dolna połowa", roi)
cv2.waitKey(0)
cv2.destroyAllWindows()