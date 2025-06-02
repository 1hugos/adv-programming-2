import cv2
import numpy as np

IMAGE_PATH = "./data/aussie_low_q.jpg"

image = cv2.imread(IMAGE_PATH)

if image is None:
    print("Błąd: nie można wczytać obrazu!")
    exit()
else:
    print("Obraz wczytano poprawnie.")

mask = np.zeros(image.shape[:2], dtype="uint8")
cv2.rectangle(mask, (50, 50), (150, 150), 255, -1)

B, G, R = cv2.split(image)

R_masked = R.copy()

red_values = R_masked[mask == 255]
red_values = cv2.add(red_values, 50)
R_masked[mask == 255] = np.clip(R_masked[mask == 255] + 50, 0, 255)

result = cv2.merge([B, G, R_masked])

cv2.imshow("Maskowany i wzmocniony kanał czerwony", result)
cv2.waitKey(0)
cv2.destroyAllWindows()