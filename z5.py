import cv2
import numpy as np

IMAGE_PATH = "./data/aussie_low_q.jpg"
IMAGE2_PATH = "./data/aussie_low_q_2.jpg"

image1 = cv2.imread(IMAGE_PATH)
image2 = cv2.imread(IMAGE2_PATH)

if image1 is None or image2 is None:
    print("Błąd: nie można wczytać obrazu!")
    exit()
else:
    print("Obraz wczytano poprawnie.")

diff = cv2.absdiff(image1, image2)
cv2.imshow("Różnice między obrazami", diff)
cv2.waitKey(0)
cv2.destroyAllWindows()
