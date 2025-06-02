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
blurred = cv2.GaussianBlur(gray, (7, 7), 0)
_, thresh_blur = cv2.threshold(blurred, 100, 255, cv2.THRESH_BINARY)
_, thresh_no_blur = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)

kernel = np.ones((3, 3), np.uint8)
erosioned = cv2.erode(thresh_blur, kernel, iterations=1)

cv2.imshow("Po erozji", erosioned)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Zniknęły nieporządane pixele