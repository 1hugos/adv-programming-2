import cv2
import numpy as np
import imutils

TEMPLATE_PATH = "./data/fanta_logo.jpg"
IMAGE_PATH = "./data/fanta.jpg"

template = cv2.imread(IMAGE_PATH)
image = cv2.imread(IMAGE_PATH)

if image is None or template is None:
    print("Błąd: nie można wczytać obrazu!")
    exit()
else:
    print("Obraz wczytano poprawnie.")

image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

result = cv2.matchTemplate(image_gray, template_gray, cv2.TM_CCOEFF_NORMED)
(minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(result)

startX, startY = maxLoc
endX = startX + template.shape[1]
endY = startY + template.shape[0]

cv2.rectangle(image, (startX, startY), (endX, endY), (0, 0, 255), 2)

print(f"Współrzędne: {(startX, startY)}, wartość dopasowania: {maxVal:.4f}")

cv2.imshow("Detekcja logo Fanty", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
