import cv2
import numpy as np

IMAGE_PATH = "./data/aussie_low_q.jpg"

image = cv2.imread(IMAGE_PATH)

if image is None:
    print("Błąd: nie można wczytać obrazu!")
    exit()
else:
    print("Obraz wczytano poprawnie.")

M = np.ones(image.shape, dtype="uint8") * 150
opencv_added = cv2.add(image, M)
numpy_added = image + 150

cv2.imshow("Przepalenie OpenCV", opencv_added)
cv2.imshow("Przepalenie NumPy", numpy_added)
cv2.waitKey(0)
cv2.destroyAllWindows()