import cv2
import numpy as np

IMAGE_PATH = "./data/aussie_low_q.jpg"

image = cv2.imread(IMAGE_PATH)

if image is None:
    print("Błąd: nie można wczytać obrazu!")
    exit()
else:
    print("Obraz wczytano poprawnie.")

cv2.imshow("Oryginalny obraz z krawędziami i szumem", image)

params = [(11, 21, 7), (11, 41, 21), (11, 61, 39)]

for d, sc, ss in params:
    filtered = cv2.bilateralFilter(image, d, sc, ss)
    title = f"Rozmycie dwustronne: d={d}, σ_kolor={sc}, σ_przestrzeń={ss}"
    cv2.imshow(title, filtered)
    cv2.waitKey(0)

cv2.destroyAllWindows()

# Odpowiedzi:
# i. Tak, skutecznie redukuje szum
# ii. Tak, lepiej niż inne metody zachowuje krawędzie
# iii. Najlepsze efekty: (11, 41, 21) – balans między rozmyciem a zachowaniem detali
