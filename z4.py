import cv2
import imutils

IMAGE_PATH = "./data/aussie_low_q.jpg"

image = cv2.imread(IMAGE_PATH)

if image is None:
    print("Błąd: nie można wczytać obrazu!")
    exit()
else:
    print("Obraz wczytano poprawnie.")

methods = [
    ("INTER_NEAREST", cv2.INTER_NEAREST),
    ("INTER_LINEAR", cv2.INTER_LINEAR),
    ("INTER_CUBIC", cv2.INTER_CUBIC),
    ("INTER_LANCZOS4", cv2.INTER_LANCZOS4),
]

for name, method in methods:
    resized = imutils.resize(image, width=image.shape[1] * 3, inter=method)
    cv2.imshow(f"Interpolacja: {name}", resized)
    cv2.waitKey(0)
cv2.destroyAllWindows()
