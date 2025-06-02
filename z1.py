import cv2
import numpy as np

IMAGE_PATH = "./data/aussie_low_q.jpg"

image = cv2.imread(IMAGE_PATH)

if image is None:
    print("Błąd: nie można wczytać obrazu!")
    exit()
else:
    print("Obraz wczytano poprawnie.")

M = np.ones(image.shape, dtype="uint8") * 50
opencv_added = cv2.add(image, M)
numpy_added = image + 50

cv2.imshow("OpenCV Dodawanie", opencv_added)
cv2.imshow("NumPy Dodawanie", numpy_added)
cv2.waitKey(0)
cv2.destroyAllWindows()
