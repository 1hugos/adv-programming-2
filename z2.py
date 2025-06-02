import cv2
import numpy as np

IMAGE_PATH = "./data/brick.jpg"

image = cv2.imread(IMAGE_PATH)

if image is None:
    print("Błąd: nie można wczytać obrazu!")
    exit()
else:
    print("Obraz wczytano poprawnie.")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (7, 7), 0)

block_sizes = [11, 21, 31, 41]

for block_size in block_sizes:
    thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                                   cv2.THRESH_BINARY_INV, block_size, 10)
    cv2.imshow(f"blockSize={block_size}", thresh)
    cv2.waitKey(0)

cv2.destroyAllWindows()

# Najlepiej wypadł rozmiar 11