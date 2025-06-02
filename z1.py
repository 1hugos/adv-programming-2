import cv2
import numpy as np

IMAGE_PATH = "./data/aussie_low_q.jpg"

image = cv2.imread(IMAGE_PATH)

if image is None:
    print("Błąd: nie można wczytać obrazu!")
    exit()
else:
    print("Obraz wczytano poprawnie.")

cv2.imshow("RGB - obraz oryginalny", image)

for (name, channel) in zip(("B", "G", "R"), cv2.split(image)):
    cv2.imshow(f"Kanał {name}", channel)

hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
cv2.imshow("HSV - obraz", hsv_image)

for (name, channel) in zip(("H", "S", "V"), cv2.split(hsv_image)):
    cv2.imshow(f"Kanał {name}", channel)

cv2.waitKey(0)
cv2.destroyAllWindows()