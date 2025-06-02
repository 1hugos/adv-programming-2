import cv2

IMAGE_PATH = "./data/aussie_low_q.jpg"

image = cv2.imread(IMAGE_PATH)

if image is None:
    print("Błąd: nie można wczytać obrazu!")
    exit()
else:
    print("Obraz wczytano poprawnie.")

try:
    flip_code = int(input("Podaj sposób odbicia (0=pionowe, 1=poziome, -1=oba): "))
    if flip_code in [0, 1, -1]:
        flipped = cv2.flip(image, flip_code)
        cv2.imshow("Wynik odbicia", flipped)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("Nieprawidłowy kod. Użyj 0, 1 lub -1.")
except ValueError:
    print("Musisz podać liczbę całkowitą.")