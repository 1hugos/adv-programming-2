import cv2

IMAGE_PATH = "./data/aussie_low_q.jpg"

image = cv2.imread(IMAGE_PATH)

if image is None:
    print("Błąd: nie można wczytać obrazu!")
    exit()
else:
    print("Obraz wczytano poprawnie.")

flipped = cv2.flip(image, -1)

cv2.imshow("Odbicie względem obu osi", flipped)
cv2.waitKey(0)
cv2.destroyAllWindows()
