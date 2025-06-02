import cv2

IMAGE_PATH = "./data/aussie_low_q.jpg"

image = cv2.imread(IMAGE_PATH)

if image is None:
    print("Błąd: nie można wczytać obrazu!")
    exit()
else:
    print("Obraz wczytano poprawnie.")

(h, w) = image.shape[:2]
right_half = image[:, w // 2:]
flipped_half = cv2.flip(right_half, 1)
image[:, w // 2:] = flipped_half

cv2.imshow("Odbicie prawej połowy", image)
cv2.waitKey(0)
cv2.destroyAllWindows()