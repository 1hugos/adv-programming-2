import cv2
import numpy as np

IMAGE_PATH = "./data/face.jpg"

image = cv2.imread(IMAGE_PATH)

if image is None:
    print("Błąd: nie można wczytać obrazu!")
    exit()
else:
    print("Obraz wczytano poprawnie.")

image = cv2.resize(image, (500, 650))
cv2.imshow("Oryginał", image)

mask = np.ones(image.shape[:2], dtype="uint8") * 255
cv2.rectangle(mask, (160, 160), (360, 210), 0, -1)

masked = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow("Oczy ukryte maską", masked)
cv2.waitKey(0)
cv2.destroyAllWindows()
