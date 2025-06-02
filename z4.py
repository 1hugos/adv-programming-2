import cv2
import numpy as np

IMAGE_PATH = "./data/aussie_low_q.jpg"

image = cv2.imread(IMAGE_PATH)

if image is None:
    print("Błąd: nie można wczytać obrazu!")
    exit()
else:
    print("Obraz wczytano poprawnie.")

cv2.imshow("Tekst z przerwami", image)

kernel_sizes = [(3, 3), (5, 5)]
kernel_shapes = {"prostokątny": cv2.MORPH_RECT, "eliptyczny": cv2.MORPH_ELLIPSE}

for name, shape in kernel_shapes.items():
    for size in kernel_sizes:
        kernel = cv2.getStructuringElement(shape, size)
        closed = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
        cv2.imshow(f"Zamknięcie - {name}, kernel {size[0]}x{size[1]}", closed)
        cv2.waitKey(0)

cv2.destroyAllWindows()
