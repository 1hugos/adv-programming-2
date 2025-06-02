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

(h, w) = image.shape[:2]
center = (w // 2, h // 2)

M = cv2.getRotationMatrix2D(center, 60, 1.0)
rotated_cv = cv2.warpAffine(image, M, (w, h))

rotated_imutils = imutils.rotate(image, 60)

cv2.imshow("Rotacja 60 stopni (warpAffine)", rotated_cv)
cv2.imshow("Rotacja 60 stopni (imutils.rotate)", rotated_imutils)
cv2.waitKey(0)
cv2.destroyAllWindows()