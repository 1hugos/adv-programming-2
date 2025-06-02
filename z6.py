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
cnts, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

filtered_cnts = []
for c in cnts:
    area = cv2.contourArea(c)
    if 500 < area < 5000:
        filtered_cnts.append(c)

output = resized.copy()
cv2.drawContours(output, filtered_cnts, -1, (255, 0, 0), 2)
print(f"Liczba konturów po filtracji: {len(filtered_cnts)}")

cv2.imshow("Kontury po filtracji", output)
cv2.waitKey(0)
cv2.destroyAllWindows()