import cv2
import numpy as np

IMAGE_PATH = "./data/aussie_low_q.jpg"
image = cv2.imread(IMAGE_PATH)

if image is None:
    print("Błąd: nie można wczytać obrazu!")
    exit()
else:
    print("Obraz wczytano poprawnie.")

p1 = image[50, 50]
p2 = image[200, 200]

print(f"Piksel 1 (50,50): {p1}")
print(f"Piksel 2 (200,200): {p2}")
print(f"Różnica R: {abs(int(p1[2]) - int(p2[2]))}")
print(f"Różnica G: {abs(int(p1[1]) - int(p2[1]))}")
print(f"Różnica B: {abs(int(p1[0]) - int(p2[0]))}")