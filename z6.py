import cv2
import numpy as np

IMAGE_PATH = "./data/opencv_logo.jpg"

image = cv2.imread(IMAGE_PATH)

if image is None:
    print("Błąd: nie można wczytać obrazu!")
    exit()
else:
    print("Obraz wczytano poprawnie.")

B, G, R = cv2.split(image)

swapped_logo = cv2.merge([R, G, B])
cv2.imshow("Zamieniony kanał niebieski i czerwony", swapped_logo)

G_zero = np.zeros_like(G)
logo_no_green = cv2.merge([B, G_zero, R])
cv2.imshow("Usunięty kanał zielony", logo_no_green)

cv2.waitKey(0)
cv2.destroyAllWindows()
