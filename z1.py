import cv2

IMAGE_PATH = "./data/aussie_low_q.jpg"

image = cv2.imread(IMAGE_PATH)

if image is None:
    print("Błąd: nie można wczytać obrazu!")
    exit()
else:
    print("Obraz wczytano poprawnie.")

(h, w) = image.shape[:2]
new_dim = (w // 2, h // 2)

resized = cv2.resize(image, new_dim, interpolation=cv2.INTER_AREA)
cv2.imshow("Zmniejszony o połowę", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()