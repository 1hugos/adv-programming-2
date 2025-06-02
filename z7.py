import cv2
import numpy as np
import imutils

IMAGE_PATH = "./data/brick.jpg"

image = cv2.imread(IMAGE_PATH)

if image is None:
    print("Błąd: nie można wczytać obrazu!")
    exit()
else:
    print("Obraz wczytano poprawnie.")

resized = imutils.resize(image, width=300)
gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(gray, 140, 255, cv2.THRESH_BINARY)
cnts, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

filtered_cnts = []
widths = []
heights = []

for c in cnts:
    area = cv2.contourArea(c)
    if 500 < area < 5000:
        filtered_cnts.append(c)
        x, y, w, h = cv2.boundingRect(c)
        widths.append(w)
        heights.append(h)

count = len(filtered_cnts)
mean_width = int(np.mean(widths)) if widths else 0
mean_height = int(np.mean(heights)) if heights else 0
min_size = (min(widths), min(heights)) if widths and heights else (0, 0)
max_size = (max(widths), max(heights)) if widths and heights else (0, 0)

print("Raport detekcji kostek:")
print(f"Liczba wykrytych kostek: {count}")
print(f"Średnia szerokość: {mean_width} px")
print(f"Średnia wysokość: {mean_height} px")
print(f"Minimalny rozmiar: {min_size[0]}x{min_size[1]} px")
print(f"Maksymalny rozmiar: {max_size[0]}x{max_size[1]} px")