import cv2
import numpy as np
import matplotlib.pyplot as plt

IMAGE_PATH = "./data/opencv_logo.jpg"

image = cv2.imread(IMAGE_PATH)

if image is None:
    print("Błąd: nie można wczytać obrazu!")
    exit()
else:
    print("Obraz wczytano poprawnie.")

cv2.imshow("Oryginalny obraz tekstu", image)

kernel_sizes = [(3, 3), (9, 9), (15, 15)]

for (kX, kY) in kernel_sizes:
    cv2.imshow(f"Tekst - rozmycie uśrednione ({kX}x{kY})", cv2.blur(image, (kX, kY)))
    cv2.imshow(f"Tekst - rozmycie Gaussa ({kX}x{kY})", cv2.GaussianBlur(image, (kX, kY), 0))
    if kX == kY:
        cv2.imshow(f"Tekst - rozmycie medianowe ({kX})", cv2.medianBlur(image, kX))
    cv2.waitKey(0)

cv2.imshow("Tekst - rozmycie dwustronne", cv2.bilateralFilter(image, 11, 41, 21))
cv2.waitKey(0)
cv2.destroyAllWindows()

# Odpowiedzi:
# i. Najmocniej rozmywa tekst: uśrednione
# ii. Najlepsza czytelność: medianowe