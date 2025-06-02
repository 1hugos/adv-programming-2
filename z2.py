import cv2
import numpy as np

IMAGE_PATH = "./data/aussie_low_q.jpg"

image = cv2.imread(IMAGE_PATH)

if image is None:
    print("Błąd: nie można wczytać obrazu!")
    exit()
else:
    print("Obraz wczytano poprawnie.")


kernel_sizes = [(3, 3), (5, 5), (9, 9), (15, 15)]

for (kX, kY) in kernel_sizes:
    cv2.imshow(f"Uśrednione ({kX}x{kY})", cv2.blur(image, (kX, kY)))
    cv2.imshow(f"Gaussowskie ({kX}x{kY})", cv2.GaussianBlur(image, (kX, kY), 0))
    if kX == kY:
        cv2.imshow(f"Medianowe ({kX})", cv2.medianBlur(image, kX))
    cv2.waitKey(0)

cv2.destroyAllWindows()

# Odpowiedzi:
# i. Im większy kernel, tym bardziej rozmyty obraz
# ii. Optymalny rozmiar to 3x3 lub 5x5