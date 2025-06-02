import cv2
import numpy as np

IMAGE_PATH = "./data/aussie_low_q.jpg"

image = cv2.imread(IMAGE_PATH)

if image is None:
    print("Błąd: nie można wczytać obrazu!")
    exit()
else:
    print("Obraz wczytano poprawnie.")

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(hsv)
s_lower = cv2.subtract(s, 50)
s_higher = cv2.add(s, 50)
low_sat_img = cv2.cvtColor(cv2.merge([h, s_lower, v]), cv2.COLOR_HSV2BGR)
high_sat_img = cv2.cvtColor(cv2.merge([h, s_higher, v]), cv2.COLOR_HSV2BGR)

cv2.imshow("Obniżona saturacja", low_sat_img)
cv2.imshow("Podwyższona saturacja", high_sat_img)
cv2.waitKey(0)
cv2.destroyAllWindows()