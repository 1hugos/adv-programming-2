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

cell_h, cell_w = h // 3, w // 3
for y in range(3):
    for x in range(3):
        roi = image[y * cell_h:(y + 1) * cell_h, x * cell_w:(x + 1) * cell_w]
        cv2.imshow(f"Fragment ({y},{x})", roi)
        cv2.waitKey(0)
cv2.destroyAllWindows()