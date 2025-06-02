import cv2
import imutils

IMAGE_PATH = "./data/aussie_low_q.jpg"

image = cv2.imread(IMAGE_PATH)

if image is None:
    print("Błąd: nie można wczytać obrazu!")
    exit()
else:
    print("Obraz wczytano poprawnie.")

resized = imutils.resize(image, width=800)
cv2.imwrite("resized_output.jpg", resized)
cv2.imshow("Powiększony do szerokości 800 px", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
