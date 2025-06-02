import cv2
import numpy as np

IMAGE_PATH = "./data/aussie_low_q.jpg"

image = cv2.imread(IMAGE_PATH)

if image is None:
    print("Błąd: nie można wczytać obrazu!")
    exit()
else:
    print("Obraz wczytano poprawnie.")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

for T in [30, 100, 200]:
    _, thresh = cv2.threshold(gray, T, 255, cv2.THRESH_BINARY)
    cv2.imshow(f"Progowanie T={T}", thresh)

cv2.waitKey(0)
cv2.destroyAllWindows()

# Najlepiej oddzeila pierwsz plan od tła progowanie z wartością 100