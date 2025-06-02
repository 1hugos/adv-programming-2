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
brighter = cv2.add(gray, 50)
_, otsu_thresh = cv2.threshold(brighter, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
cv2.imshow("Otsu", otsu_thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Wynik z wykorzystaniem tej metody dał o wiele lepszy rezulat