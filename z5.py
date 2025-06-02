import cv2
import numpy as np

IMAGE_PATH = "./data/opencv_logo.jpg"

image = cv2.imread(IMAGE_PATH)

if image is None:
    print("Błąd: nie można wczytać obrazu!")
    exit()
else:
    print("Obraz wczytano poprawnie.")

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
lower_green = np.array([40, 50, 50])
upper_green = np.array([80, 255, 255])
mask = cv2.inRange(hsv, lower_green, upper_green)
result = cv2.bitwise_and(image, image, mask=mask)

cv2.imshow("Zielone obiekty - maska", mask)
cv2.imshow("Zielone obiekty - wynik", result)
cv2.waitKey(0)
cv2.destroyAllWindows()