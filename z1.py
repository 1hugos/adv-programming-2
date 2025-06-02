import cv2
import numpy as np

IMAGE_PATH = "./data/aussie_low_q.jpg"

image = cv2.imread(IMAGE_PATH)

if image is None:
    print("Błąd: nie można wczytać obrazu!")
    exit()
else:
    print("Obraz wczytano poprawnie.")

cv2.imshow("Oryginalny obraz", image)

kernel_sizes = [(3, 3), (9, 9), (15, 15)]

# Średnie rozmycie
for kX, kY in kernel_sizes:
    blurred = cv2.blur(image, (kX, kY))
    cv2.imshow("Rozmycie uśrednione ({}x{})".format(kX, kY), blurred)
    cv2.waitKey(0)

# Rozmycie Gaussa
for kX, kY in kernel_sizes:
    blurred = cv2.GaussianBlur(image, (kX, kY), 0)
    cv2.imshow("Rozmycie Gaussa ({}x{})".format(kX, kY), blurred)
    cv2.waitKey(0)

# Rozmycie medianowe
for k in (3, 9, 15):
    blurred = cv2.medianBlur(image, k)
    cv2.imshow("Rozmycie medianowe ({})".format(k), blurred)
    cv2.waitKey(0)

# Rozmycie dwustronne
params = [(11, 21, 7), (11, 41, 21), (11, 61, 39)]
for d, sc, ss in params:
    blurred = cv2.bilateralFilter(image, d, sc, ss)
    title = "Rozmycie dwustronne d={}, σ_kolor={}, σ_przestrzeń={}".format(d, sc, ss)
    cv2.imshow(title, blurred)
    cv2.waitKey(0)

cv2.destroyAllWindows()

# Odpowiedzi
# i. Najlepiej usuwa szum: rozmycie medianowe
# ii. Najwięcej szczegółów zachowuje: rozmycie dwustronne
# iii. Zalety i wady:
# - cv2.blur: szybkie, ale rozmywa krawędzie
# - cv2.GaussianBlur: lepsze od zwykłego rozmycia, ale wciąż gubi krawędzie
# - cv2.medianBlur: skuteczne na szum typu sól i pieprz, zachowuje kontury
# - cv2.bilateralFilter: zachowuje krawędzie, ale wolne przy dużych obrazach
