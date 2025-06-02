import cv2
import numpy as np

IMAGE_PATH = "./data/flower.jpg"

image = cv2.imread(IMAGE_PATH)

if image is None:
    print("Błąd: nie można wczytać obrazu!")
    exit()
else:
    print("Obraz wczytano poprawnie.")

image = cv2.resize(image, (500, 650))
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

lower_red1 = np.array([0, 120, 70])
upper_red1 = np.array([10, 255, 255])
mask1 = cv2.inRange(hsv, lower_red1, upper_red1)

lower_red2 = np.array([170, 120, 70])
upper_red2 = np.array([180, 255, 255])
mask2 = cv2.inRange(hsv, lower_red2, upper_red2)

mask = cv2.bitwise_or(mask1, mask2)

result = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow("Tylko czerwony kolor", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
