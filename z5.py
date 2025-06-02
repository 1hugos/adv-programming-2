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

kernel_sizes = [(5, 5)]
kernel_shapes = {
    "kwadrat": cv2.MORPH_RECT,
    "krzyż": cv2.MORPH_CROSS,
    "elipsa": cv2.MORPH_ELLIPSE,
}

operations = {
    "Erozja": cv2.erode,
    "Dylatacja": cv2.dilate,
    "Otwarcie": lambda img, kernel: cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel),
    "Zamknięcie": lambda img, kernel: cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel),
    "Gradient": lambda img, kernel: cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel),
}

for kernel_name, kernel_shape in kernel_shapes.items():
    kernel = cv2.getStructuringElement(kernel_shape, kernel_sizes[0])
    for op_name, op_func in operations.items():
        if op_name in ["Erozja", "Dylatacja"]:
            result = op_func(image, kernel, iterations=1)
        else:
            result = op_func(image, kernel)
        cv2.imshow(f"{op_name} - {kernel_name}", result)
        cv2.waitKey(0)

cv2.destroyAllWindows()
