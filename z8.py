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

for x in range(0, w - 100, 10):
    roi = image[0:100, x:x + 100]
    cv2.imshow("Przesuwające się ROI", roi)
    key = cv2.waitKey(0)
    if key == 27:
        break
cv2.destroyAllWindows()