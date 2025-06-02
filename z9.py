import cv2
import numpy as np

IMAGE_PATH = "./data/aussie_low_q.jpg"
image = cv2.imread(IMAGE_PATH)

if image is None:
    print("Błąd: nie można wczytać obrazu!")
    exit()
else:
    print("Obraz wczytano poprawnie.")

image_before = image.copy()
image_after = image.copy()

image_after[50:101, 50:101] = [255, 255, 255]

cv2.imshow("Przed", image_before)
cv2.imshow("Po", image_after)
cv2.waitKey(0)
cv2.destroyAllWindows()
