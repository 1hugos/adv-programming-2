import cv2

IMAGE_PATH = "./data/aussie_low_q.jpg"

image = cv2.imread(IMAGE_PATH)

if image is None:
    print("Błąd: nie można wczytać obrazu!")
    exit()
else:
    print("Obraz wczytano poprawnie.")

resized = cv2.resize(image, (200, 300), interpolation=cv2.INTER_AREA)
cv2.imshow("Rozmiar 200x300", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
