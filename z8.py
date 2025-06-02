import cv2

IMAGE_PATH = "./data/aussie_low_q.jpg"

image = cv2.imread(IMAGE_PATH)

if image is None:
    print("Błąd: nie można wczytać obrazu!")
    exit()
else:
    print("Obraz wczytano poprawnie.")

(h, w) = image.shape[:2]
new_dim = (w * 4, h * 4)

resized_cubic = cv2.resize(image, new_dim, interpolation=cv2.INTER_CUBIC)
resized_lanczos = cv2.resize(image, new_dim, interpolation=cv2.INTER_LANCZOS4)

cv2.imshow("Powiększony 4x (INTER_CUBIC)", resized_cubic)
cv2.imshow("Powiększony 4x (INTER_LANCZOS4)", resized_lanczos)
cv2.waitKey(0)
cv2.destroyAllWindows()