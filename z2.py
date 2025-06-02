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

for angle in [30, 45]:
    rotated = imutils.rotate(image, angle)
    rotated_gray = cv2.cvtColor(rotated, cv2.COLOR_BGR2GRAY)
    result = cv2.matchTemplate(rotated_gray, template_gray, cv2.TM_CCOEFF_NORMED)
    _, maxVal, _, maxLoc = cv2.minMaxLoc(result)

    print(f"Obrót: {angle}°, maxVal: {maxVal:.4f}")

    if maxVal > 0.6:
        startX, startY = maxLoc
        endX = startX + template.shape[1]
        endY = startY + template.shape[0]
        cv2.rectangle(rotated, (startX, startY), (endX, endY), (0, 255, 0), 2)
        cv2.imshow(f"Rotated {angle} degrees", rotated)
        cv2.waitKey(0)
cv2.destroyAllWindows()
