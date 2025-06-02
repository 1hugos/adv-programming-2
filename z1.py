import cv2
import numpy as np

IMAGE_PATH = "./data/brick.jpg"

image = cv2.imread(IMAGE_PATH)

if image is None:
    print("Błąd: nie można wczytać obrazu!")
    exit()
else:
    print("Obraz wczytano poprawnie.")

cv2.imshow("Oryginalny obraz", image)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (7, 7), 0)

_, simple_thresh = cv2.threshold(blurred, 100, 255, cv2.THRESH_BINARY_INV)
_, otsu_thresh = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

adaptive_mean = cv2.adaptiveThreshold(
    blurred, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 21, 10
)

adaptive_gaussian = cv2.adaptiveThreshold(
    blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 21, 10
)

cv2.imshow("Proste progowanie (T=100)", simple_thresh)
cv2.imshow("Progowanie Otsu", otsu_thresh)
cv2.imshow("Progowanie adaptacyjne Mean", adaptive_mean)
cv2.imshow("Progowanie adaptacyjne Gaussian", adaptive_gaussian)

cv2.waitKey(0)
cv2.destroyAllWindows()

# Najlepiej wypadło progowanie adaptacyjne Gaussian oraz Mean