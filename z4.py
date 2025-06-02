import cv2

IMAGE_PATH = "./data/aussie_low_q.jpg"

image = cv2.imread(IMAGE_PATH)

if image is None:
    print("Błąd: nie można wczytać obrazu!")
    exit()
else:
    print("Obraz wczytano poprawnie.")

flipped_h = cv2.flip(image, 1)
flipped_v = cv2.flip(image, 0)
flipped_both = cv2.flip(image, -1)

cv2.imshow("Oryginał", image)
cv2.imshow("Poziome", flipped_h)
cv2.imshow("Pionowe", flipped_v)
cv2.imshow("Obie osie", flipped_both)
cv2.waitKey(0)
cv2.destroyAllWindows()