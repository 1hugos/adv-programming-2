import cv2
import numpy as np

IMAGE_PATH = "./data/aussie_low_q.jpg"

image = cv2.imread(IMAGE_PATH)

if image is None:
    print("Błąd: nie można wczytać obrazu!")
    exit()
else:
    print("Obraz wczytano poprawnie.")

M = np.ones(image.shape, dtype="uint8") * 80
opencv_sub = cv2.subtract(image, M)
numpy_sub = image - 80

cv2.imshow("Przyciemniony OpenCV", opencv_sub)
cv2.imshow("Przyciemniony NumPy", numpy_sub)
cv2.waitKey(0)
cv2.destroyAllWindows()