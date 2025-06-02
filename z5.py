import cv2
import numpy as np

IMAGE_PATH = "./data/aussie_low_q.jpg"
image = cv2.imread(IMAGE_PATH)

if image is None:
    print("Błąd: nie można wczytać obrazu!")
    exit()
else:
    print("Obraz wczytano poprawnie.")


try:
    tx = int(input("Podaj przesunięcie w osi X (px): "))
    ty = int(input("Podaj przesunięcie w osi Y (px): "))
except ValueError:
    print("Niepoprawne dane wejściowe!")
    exit()

cv2.imshow("Oryginalny", image)

M = np.float32([[1, 0, tx], [0, 1, ty]])
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))

cv2.imshow(f"Przesunięto o ({tx}, {ty})", shifted)
cv2.waitKey(0)
cv2.destroyAllWindows()
