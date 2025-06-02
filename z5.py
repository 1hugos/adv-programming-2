import cv2
import numpy as np
import matplotlib.pyplot as plt

IMAGE_PATH = "./data/aussie_low_q.jpg"

image = cv2.imread(IMAGE_PATH)

if image is None:
    print("Błąd: nie można wczytać obrazu!")
    exit()
else:
    print("Obraz wczytano poprawnie.")

noise_image = image.copy()
noise_image = cv2.randn(noise_image, (0, 0, 0), (20, 20, 20)) + image

cv2.imshow("Obraz z szumem Gaussa", noise_image)

blur = cv2.blur(noise_image, (5, 5))
gauss = cv2.GaussianBlur(noise_image, (5, 5), 0)
median = cv2.medianBlur(noise_image, 5)
bilateral = cv2.bilateralFilter(noise_image, 9, 75, 75)

cv2.imshow("Rozmycie - uśrednione", blur)
cv2.imshow("Rozmycie - Gaussa", gauss)
cv2.imshow("Rozmycie - medianowe", median)
cv2.imshow("Rozmycie - dwustronne", bilateral)
 
cv2.waitKey(0)
cv2.destroyAllWindows()

# Odpowiedzi:
# Najlepiej usuwa szum: uśrednione