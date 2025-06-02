import cv2
import numpy as np

IMAGE_PATH = "./data/aussie_low_q.jpg"
image = cv2.imread(IMAGE_PATH)

if image is None:
    print("Błąd: nie można wczytać obrazu!")
    exit()
else:
    print("Obraz wczytano poprawnie.")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(gray)
brightest_pixel = image[max_loc[1], max_loc[0]]

print(f"Najjaśniejszy piksel: {brightest_pixel} na pozycji {max_loc}")
