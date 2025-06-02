import cv2
import numpy as np

IMAGE_PATH = "./data/aussie_low_q.jpg"
image = cv2.imread(IMAGE_PATH)

if image is None:
    print("Błąd: nie można wczytać obrazu!")
    exit()
else:
    print("Obraz wczytano poprawnie.")

h, w = image.shape[:2]
cX, cY = w // 2, h // 2

new_image = image.copy()

startX, startY = cX - 50, cY - 50
endX, endY = cX + 50, cY + 50

cv2.rectangle(new_image, (startX, startY), (endX, endY), (0, 0, 255), -1)

cv2.imshow("Czerwony kwadrat", new_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
