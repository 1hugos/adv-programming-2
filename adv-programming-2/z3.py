import cv2

IMAGE_PATH = "./data/dog.jpg"

image_grey = cv2.imread(IMAGE_PATH, cv2.IMREAD_GRAYSCALE)

if image_grey is None:
    print("Błąd: nie można wczytać obrazu!")
else:
    print("Obraz wczytano poprawnie.")


(h, w) = image_grey.shape[:3]
print(f"Liczba kanałów dla szarego zdjęcia do 1")

resized_image = cv2.resize(image_grey, (1024, 768))

cv2.imshow("Wyświetlony obraz", resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
