import cv2
import numpy as np

IMAGE_PATH = "./data/flower.jpg"

image = cv2.imread(IMAGE_PATH)

if image is None:
    print("Błąd: nie można wczytać obrazu!")
    exit()
else:
    print("Obraz wczytano poprawnie.")

B, G, R = cv2.split(image)

cv2.imshow("Kanał niebieski", B)
cv2.imshow("Kanał zielony", G)
cv2.imshow("Kanał czerwony", R)

cv2.imwrite("blue_channel.jpg", B)
cv2.imwrite("green_channel.jpg", G)
cv2.imwrite("red_channel.jpg", R)

cv2.waitKey(0)
cv2.destroyAllWindows()
