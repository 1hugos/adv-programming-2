import cv2
import numpy as np

IMAGE_PATH = "./data/aussie_low_q.jpg"

image = cv2.imread(IMAGE_PATH)

if image is None:
    print("Błąd: nie można wczytać obrazu!")
    exit()
else:
    print("Obraz wczytano poprawnie.")

B, G, R = cv2.split(image)

R_enhanced = cv2.add(R, 50)

enhanced_image = cv2.merge([B, G, R_enhanced])

cv2.imshow("Wzmocniony kanał czerwony", enhanced_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
