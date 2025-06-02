import cv2

IMAGE_PATH = "./data/aussie_low_q.jpg"

image = cv2.imread(IMAGE_PATH)

if image is None:
    print("Błąd: nie można wczytać obrazu!")
    exit()
else:
    print("Obraz wczytano poprawnie.")

new_image = image.copy()

height, width, _ = new_image.shape

new_image[height - 1, width - 1] = (0, 0, 255)

resized_image = cv2.resize(image, (1024, 768))
resized_new_image = cv2.resize(new_image, (1024, 768))

cv2.imshow("Oryginalny obraz", resized_image)
cv2.imshow("Obraz po zmianie piksela", resized_new_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
