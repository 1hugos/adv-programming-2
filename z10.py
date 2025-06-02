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

for angle in range(0, 361, 15):
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(image, M, (w, h))
    cv2.imshow("Obracanie w pętli", rotated)
    key = cv2.waitKey(500)
    if key == 27:
        break

cv2.destroyAllWindows()