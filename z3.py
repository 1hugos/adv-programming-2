import cv2
import numpy as np

IMAGE_PATH = "./data/aussie_low_q.jpg"
image = cv2.imread(IMAGE_PATH)

if image is None:
    print("Błąd: nie można wczytać obrazu!")
    exit()
else:
    print("Obraz wczytano poprawnie.")

cv2.imshow("Oryginalny", image)

width = image.shape[1]
height = image.shape[0]

tx = int(width * 0.6)
ty = int(height * 0.7)

M = np.float32([[1, 0, tx], [0, 1, ty]])
shifted = cv2.warpAffine(image, M, (width, height))

cv2.imshow(f"Przesunięty o {tx}px w prawo i o {ty}px w dół", shifted)
cv2.waitKey(0)
cv2.destroyAllWindows()
