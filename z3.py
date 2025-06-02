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

gray_orig = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

sizes = [600, 400, 300, 200]

for size in sizes:
    resized = imutils.resize(image, width=size)
    gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 140, 255, cv2.THRESH_BINARY)
    cnts, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    output = resized.copy()
    cv2.drawContours(output, cnts, -1, (0, 255, 0), 2)
    print(f"Rozmiar: {size}px, Liczba konturów: {len(cnts)}")
    cv2.imshow(f"Kontury rozmiar {size}", output)
    cv2.waitKey(0)

cv2.destroyAllWindows()