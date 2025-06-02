import cv2

IMAGE_PATH = "./data/aussie_low_q.jpg"

image = cv2.imread(IMAGE_PATH)

if image is None:
    print("Błąd: nie można wczytać obrazu!")
    exit()
else:
    print("Obraz wczytano poprawnie.")

new_image = image.copy()

h, w = new_image.shape[:2]

(cX, cY) = (w // 2, h // 2)

(b, g, r) = image[cY, cX]
print(f"Pixel o współrzędych ({cX}, {cY}) - Czerwony: {r}, Zielony: {g}, Niebieski: {b}")


