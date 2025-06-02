import cv2

IMAGE_PATH = "./data/dog.jpg"

image = cv2.imread(IMAGE_PATH)

if image is None:
    print("Błąd: nie można wczytać obrazu!")
else:
    print("Obraz wczytano poprawnie.")

(b, g, r) = image[0, 0]
print(f"Pixel o współrzędych (0, 0) - Czerwony: {r}, Zielony: {g}, Niebieski: {b}")
