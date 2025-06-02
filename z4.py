import cv2
import numpy as np
import imutils

IMAGE_PATH = "./data/aussie_low_q.jpg"
image = cv2.imread(IMAGE_PATH)

if image is None:
    print("Błąd: nie można wczytać obrazu!")
    exit()
else:
    print("Obraz wczytano poprawnie.")

cv2.imshow("Oryginalny", image)

shifted_warp = cv2.warpAffine(
    image, np.float32([[1, 0, 100], [0, 1, 50]]), (image.shape[1], image.shape[0])
)
cv2.imshow("Przesunięcie z warpAffine (100 w prawo, 50 w dół)", shifted_warp)

shifted_imutils = imutils.translate(image, 100, 50)
cv2.imshow("Przesunięcie z imutils.translate (100 w prawo, 50 w dół)", shifted_imutils)
cv2.waitKey(0)
cv2.destroyAllWindows()
