import cv2
import numpy as np
import imutils
import os

os.makedirs("kostki_wyciete", exist_ok=True)
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

for i, c in enumerate(cnts, 1):
    x, y, w, h = cv2.boundingRect(c)
    cv2.putText(resized, str(i), (x + w//2, y + h//2),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    mask = np.zeros(resized.shape[:2], dtype="uint8")
    cv2.drawContours(mask, [c], -1, 255, -1)
    segmented = cv2.bitwise_and(resized, resized, mask=mask)
    roi = segmented[y:y+h, x:x+w]

    filename = f"kostki_wyciete/kostka_{i:02d}.png"
    cv2.imwrite(filename, roi)

cv2.imshow("Numerowane kostki", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()