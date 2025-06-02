import cv2
import numpy as np

IMAGE_PATH = "./data/document.jpg"

image = cv2.imread(IMAGE_PATH)

if image is None:
    print("Błąd: nie można wczytać obrazu!")
    exit()
else:
    print("Obraz wczytano poprawnie.")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

adaptive_thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                        cv2.THRESH_BINARY_INV, 21, 10)

cv2.imshow("Oryginalny dokument", image)
cv2.imshow("Segmentacja tekstu adaptacyjna", adaptive_thresh)

cv2.waitKey(0)
cv2.destroyAllWindows()