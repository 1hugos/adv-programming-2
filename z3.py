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
lower_blue = np.array([100, 150, 0])
upper_blue = np.array([140, 255, 255])
mask = cv2.inRange(hsv, lower_blue, upper_blue)
result = cv2.bitwise_and(image, image, mask=mask)

cv2.imshow("Niebieskie obiekty - maska", mask)
cv2.imshow("Niebieskie obiekty - wynik", result)
cv2.waitKey(0)
cv2.destroyAllWindows()