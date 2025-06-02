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

C_values = [2, 5, 10, 15]
methods = [(cv2.ADAPTIVE_THRESH_MEAN_C, "Mean"),
           (cv2.ADAPTIVE_THRESH_GAUSSIAN_C, "Gaussian")]

for method, name in methods:
    for C in C_values:
        thresh = cv2.adaptiveThreshold(blurred, 255, method,
                                       cv2.THRESH_BINARY_INV, 21, C)
        cv2.imshow(f"{name} C={C}", thresh)
        cv2.waitKey(0)

cv2.destroyAllWindows()

# Najlepiej poradził sobie Mean z wartościa 10