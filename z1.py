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

mask = np.zeros(image.shape[:2], dtype="uint8")
center_x, center_y = image.shape[1] // 2, image.shape[0] // 2 - 140
cv2.ellipse(mask, (center_x, center_y), (100, 140), 0, 0, 360, 255, -1)

masked = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow("Twarz wyodrębniona maską", masked)
cv2.waitKey(0)
cv2.destroyAllWindows()
