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

h_third, w_third = h // 3, w // 3

center_crop = image[h_third:h_third*2, w_third:w_third*2]

cv2.imshow("Środkowy fragment", center_crop)
cv2.waitKey(0)
cv2.destroyAllWindows()