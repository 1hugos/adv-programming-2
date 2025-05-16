import cv2

IMAGE_PATH = "./data/dog.jpg"

image = cv2.imread(IMAGE_PATH)

if image is None:
    print("Błąd: nie można wczytać obrazu!")
else:
    print("Obraz wczytano poprawnie.")

resized_image = cv2.resize(image, (1024, 768))

(h, w, c) = image.shape[:3]
print(f"Liczba kanałów: {c}")

cv2.imshow("Wyświetlony obraz", resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
