import cv2
import numpy as np

IMAGE_PATH = "./data/aussie_low_q.jpg"

image = cv2.imread(IMAGE_PATH)

if image is None:
    print("Błąd: nie można wczytać obrazu!")
    exit()
else:
    print("Obraz wczytano poprawnie.")

(B, G, R) = cv2.split(image)
R = cv2.add(R, 30)
G = cv2.subtract(G, 20)
B = cv2.add(B, 10)
filtered = cv2.merge([B, G, R])

cv2.imshow("Filtr Instagram", filtered)
cv2.waitKey(0)
cv2.destroyAllWindows()
