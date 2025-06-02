import cv2
import numpy as np

IMAGE_PATH = "./data/aussie_low_q.jpg"

image = cv2.imread(IMAGE_PATH)

if image is None:
    print("Błąd: nie można wczytać obrazu!")
    exit()
else:
    print("Obraz wczytano poprawnie.")

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(hsv)
h = cv2.add(h, 30)  # przesunięcie odcienia
hsv_shifted = cv2.merge([h, s, v])
result = cv2.cvtColor(hsv_shifted, cv2.COLOR_HSV2BGR)

cv2.imshow("Obraz oryginalny", image)
cv2.imshow("Po zmianie odcienia H", result)
cv2.waitKey(0)
cv2.destroyAllWindows()