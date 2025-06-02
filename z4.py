import cv2

IMAGE_PATH = "./data/aussie_low_q.jpg"

# Wczytanie obrazu
image = cv2.imread(IMAGE_PATH)

if image is None:
    print("Błąd: nie można wczytać obrazu!")
    exit()
else:
    print("Obraz wczytano poprawnie.")

h, w = image.shape[:2]
print(f"Wymiary obrazu: szerokość = {w}, wysokość = {h}")

try:
    x = int(input(f"Podaj współrzędną X (0 - {w - 1}): "))
    y = int(input(f"Podaj współrzędną Y (0 - {h - 1}): "))
except ValueError:
    print("Błąd")
    exit()

if 0 <= x < w and 0 <= y < h:
    modified_image = image.copy()

    modified_image[y, x] = (0, 0, 0)
    print(f"Zmieniono piksel ({x}, {y}) na czarny.")

    resized_image = cv2.resize(image, (1024, 768))
    resized_modified = cv2.resize(modified_image, (1024, 768))

    cv2.imshow("Oryginalny obraz", resized_image)
    cv2.imshow("Po zmianie piksela na czarny", resized_modified)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Błąd")
