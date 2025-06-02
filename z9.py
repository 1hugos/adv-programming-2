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

M = cv2.getRotationMatrix2D(center, 75, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))

cv2.imwrite("rotated_output.jpg", rotated)
cv2.imshow("Obrót o 75 stopni", rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()