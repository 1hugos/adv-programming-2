import cv2
import imutils

IMAGE_PATH = "./data/aussie_low_q.jpg"

image = cv2.imread(IMAGE_PATH)

if image is None:
    print("Błąd: nie można wczytać obrazu!")
    exit()
else:
    print("Obraz wczytano poprawnie.")

resized = imutils.resize(image, height=400)
cv2.imshow("Wysokość 400 px (proporcjonalnie)", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()