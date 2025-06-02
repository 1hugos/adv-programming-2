import cv2
import numpy as np
import imutils

IMAGE_PATH = "./data/brick.jpg"

image = cv2.imread(IMAGE_PATH)

if image is None:
    print("Błąd: nie można wczytać obrazu!")
    exit()
else:
    print("Obraz wczytano poprawnie.")

resized = imutils.resize(image, width=300)
gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)

for thresh_val in [100, 140, 180]:
    _, thresh = cv2.threshold(gray, thresh_val, 255, cv2.THRESH_BINARY)
    cv2.imshow(f"Progowanie T={thresh_val}", thresh)
    cv2.waitKey(0)

cv2.destroyAllWindows()

# Najlepiej oddziela progowanie z wartoscia 100