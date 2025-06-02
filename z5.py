import cv2
import numpy as np

IMAGE_PATH = "./data/brick.jpg"

image = cv2.imread(IMAGE_PATH)

if image is None:
    print("Błąd: nie można wczytać obrazu!")
    exit()
else:
    print("Obraz wczytano poprawnie.")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (7, 7), 0)

adaptive_mask = cv2.adaptiveThreshold(
    blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 21, 10
)

masked = cv2.bitwise_and(image, image, mask=adaptive_mask)

cv2.imshow("Obraz oryginalny", image)
cv2.imshow("Maska adaptacyjna", adaptive_mask)
cv2.imshow("Wydzielone obiekty", masked)

cv2.waitKey(0)
cv2.destroyAllWindows()
