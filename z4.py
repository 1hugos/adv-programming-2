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

methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR,
           cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]

for meth in methods:
    result = cv2.matchTemplate(image_gray, template_gray, meth)
    minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(result)
    
    if meth in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left = minLoc  # dla metod SQDIFF szukamy minimum
    else:
        top_left = maxLoc  # dla innych maksimum
    
    bottom_right = (top_left[0] + template.shape[1], top_left[1] + template.shape[0])
    img_copy = image.copy()
    cv2.rectangle(img_copy, top_left, bottom_right, (0, 255, 0), 2)
    
    print(f"Metoda: {meth}, minVal: {minVal:.4f}, maxVal: {maxVal:.4f}")
    cv2.imshow(f"Metoda {meth}", img_copy)
    cv2.waitKey(0)
cv2.destroyAllWindows()