import cv2
import numpy as np

IMAGE_PATH = "./data/aussie_low_q.jpg"

image = cv2.imread(IMAGE_PATH)

if image is None:
    print("Błąd: nie można wczytać obrazu!")
    exit()
else:
    print("Obraz wczytano poprawnie.")

B, G, R = cv2.split(image)

swapped = cv2.merge([R, B, G])

cv2.imshow("Zamieniony kanał czerwony i niebieski", swapped)

G_zeroed = np.zeros_like(G)
modified = cv2.merge([B, G_zeroed, R])

cv2.imshow("Usunięty kanał zielony", modified)

cv2.waitKey(0)
cv2.destroyAllWindows()
