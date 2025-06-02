import cv2
import numpy as np
import imutils

IMAGE_PATH = "./data/brick.jpg"

image = cv2.imread(IMAGE_PATH)

if image is None:
    print("Błąd: nie można wczytać obrazu!")
    exit()
else:
    print("Obraz wczytano poprawnie.")

resized = imutils.resize(image, width=300)
gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(gray, 140, 255, cv2.THRESH_BINARY)

modes = [cv2.RETR_EXTERNAL, cv2.RETR_TREE, cv2.RETR_LIST]
mode_names = ["RETR_EXTERNAL", "RETR_TREE", "RETR_LIST"]

for mode, name in zip(modes, mode_names):
    cnts, _ = cv2.findContours(thresh.copy(), mode, cv2.CHAIN_APPROX_SIMPLE)
    output = resized.copy()
    cv2.drawContours(output, cnts, -1, (0, 0, 255), 2)
    cv2.imshow(f"Kontury - {name}", output)
    cv2.waitKey(0)

cv2.destroyAllWindows()

# RETR_EXTERNAL - wykrywa tylko zewnętrzne kontury
# RETR_TREE - tworzy pełną hierarchię konturów, w tym kontury wewnętrzne i zagnieżdżone
# RETR_LIST - wykrywa wszystkie kontury bez tworzenia hierarchii
