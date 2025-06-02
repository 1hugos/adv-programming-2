import cv2
import numpy as np

IMAGE_PATH = "./data/aussie_low_q.jpg"

image = cv2.imread(IMAGE_PATH)

if image is None:
    print("Błąd: nie można wczytać obrazu!")
    exit()
else:
    print("Obraz wczytano poprawnie.")

cv2.imshow("Obraz z szumem", image)

kernel_sizes = [(3, 3), (5, 5), (7, 7)]

for size in kernel_sizes:
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, size)
    opened = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
    cv2.imshow(f"Otwarcie - kernel {size[0]}x{size[1]}", opened)
    cv2.waitKey(0)

cv2.destroyAllWindows()
