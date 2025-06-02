import cv2
import numpy as np

IMAGE_PATH = "./data/aussie_low_q.jpg"

image = cv2.imread(IMAGE_PATH)

if image is None:
    print("Błąd: nie można wczytać obrazu!")
    exit()
else:
    print("Obraz wczytano poprawnie.")

startX = int(input("startX: "))
endX = int(input("endX: "))
startY = int(input("startY: "))
endY = int(input("endY: "))
roi = image[startY:endY, startX:endX]
cv2.imshow("Wybrany obszar ROI", roi)
cv2.waitKey(0)
cv2.destroyAllWindows()