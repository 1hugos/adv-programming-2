import cv2
import numpy as np

IMAGE_PATH = "./data/aussie_low_q.jpg"

image = cv2.imread(IMAGE_PATH)

if image is None:
    print("Błąd: nie można wczytać obrazu!")
    exit()
else:
    print("Obraz wczytano poprawnie.")

cv2.imshow("Oryginalny obraz binarny", image)

kernel_square = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
kernel_ellipse = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))

eroded_square = cv2.erode(image, kernel_square, iterations=1)
cv2.imshow("Erozja - element kwadratowy", eroded_square)

eroded_ellipse = cv2.erode(image, kernel_ellipse, iterations=1)

cv2.imshow("Erozja - element eliptyczny", eroded_ellipse)
cv2.waitKey(0)
cv2.destroyAllWindows()
