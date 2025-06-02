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

mask_red1 = cv2.inRange(hsv, np.array([0, 100, 100]), np.array([10, 255, 255]))
mask_red2 = cv2.inRange(hsv, np.array([160, 100, 100]), np.array([179, 255, 255]))
mask_green = cv2.inRange(hsv, np.array([40, 50, 50]), np.array([80, 255, 255]))
mask_blue = cv2.inRange(hsv, np.array([100, 150, 0]), np.array([140, 255, 255]))

combined_mask = cv2.bitwise_or(mask_red1, mask_red2)
combined_mask = cv2.bitwise_or(combined_mask, mask_green)
combined_mask = cv2.bitwise_or(combined_mask, mask_blue)
result = cv2.bitwise_and(image, image, mask=combined_mask)

cv2.imshow("Wielokolorowa segmentacja - maska", combined_mask)
cv2.imshow("Wielokolorowa segmentacja - wynik", result)
cv2.waitKey(0)
cv2.destroyAllWindows()