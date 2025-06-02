import cv2
import numpy as np

IMAGE_PATH = "./data/aussie_low_q.jpg"

image = cv2.imread(IMAGE_PATH)

if image is None:
    print("Błąd: nie można wczytać obrazu!")
    exit()
else:
    print("Obraz wczytano poprawnie.")

roi = image[0:300, 0:300]
cv2.imwrite("cropped_image.jpg", roi)
cv2.imshow("Zapisany obszar 300x300", roi)
cv2.waitKey(0)
cv2.destroyAllWindows()
