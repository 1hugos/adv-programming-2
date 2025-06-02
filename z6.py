import cv2
import numpy as np

IMAGE_PATH = "./data/face.jpg"

image = cv2.imread(IMAGE_PATH)

if image is None:
    print("Błąd: nie można wczytać obrazu!")
else:
    print("Obraz wczytano poprawnie.")

resized_image = cv2.resize(image, (500, 700))

cv2.circle(resized_image, (300, 200), 30, (0, 0, 255), -1)
cv2.circle(resized_image, (210, 200), 30, (0, 0, 255), -1)
cv2.rectangle(resized_image, (220, 270), (300, 300), (0, 255, 0), -1)
cv2.circle(resized_image, (250, 210), 150, (255, 0, 0), 2)

cv2.imshow("Zamazywanie", resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()