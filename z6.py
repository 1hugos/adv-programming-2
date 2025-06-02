import cv2
import numpy as np
import matplotlib.pyplot as plt

IMAGE_PATH = "./data/couple.jpg"

image = cv2.imread(IMAGE_PATH)

if image is None:
    print("Błąd: nie można wczytać obrazu!")
    exit()
else:
    print("Obraz wczytano poprawnie.")

mask = np.zeros(image.shape[:2], dtype="uint8")
cv2.rectangle(mask, (20, 100), (200, 300), 255, -1)

background_blurred = cv2.GaussianBlur(image, (21, 21), 0)
depth_effect = np.where(mask[:, :, None] == 255, image, background_blurred)

cv2.imshow("Symulowana głębia ostrości", depth_effect)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Odpowiedzi:
# Uzyskaliśmy efekt głębi ostrości: tło jest rozmyte, a główny obiekt pozostaje ostry.