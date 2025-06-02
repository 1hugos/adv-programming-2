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
_, original_thresh = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)
_, bright_thresh = cv2.threshold(brighter, 100, 255, cv2.THRESH_BINARY)

cv2.imshow("Oryginalny", original_thresh)
cv2.imshow("Rozjaśniony", bright_thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Po zbyt mocnym rozjaśnieniu stracone zostaly krawędzie elementu 