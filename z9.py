import cv2
import imutils

IMAGE_PATH = "./data/aussie_low_q.jpg"

image = cv2.imread(IMAGE_PATH)

if image is None:
    print("Błąd: nie można wczytać obrazu!")
    exit()
else:
    print("Obraz wczytano poprawnie.")

(h, w) = image.shape[:2]

for scale in range(100, 301, 20):
    width = int(w * scale / 100)
    resized = imutils.resize(image, width=width)
    cv2.imshow("Dynamiczne skalowanie", resized)
    if cv2.waitKey(500) == 27:
        break
cv2.destroyAllWindows()
