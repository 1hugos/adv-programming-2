import cv2
import numpy as np

IMAGE_PATH = "./data/couple.jpg"

image = cv2.imread(IMAGE_PATH)

if image is None:
    print("Błąd: nie można wczytać obrazu!")
    exit()
else:
    print("Obraz wczytano poprawnie.")

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
lower_skin = np.array([0, 20, 70])
upper_skin = np.array([20, 255, 255])
mask = cv2.inRange(hsv, lower_skin, upper_skin)
skin = cv2.bitwise_and(image, image, mask=mask)

cv2.imshow("Obszary skóry - maska", mask)
cv2.imshow("Obszary skóry - wynik", skin)
cv2.waitKey(0)
cv2.destroyAllWindows()