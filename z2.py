import cv2
import numpy as np
import matplotlib.pyplot as plt

IMAGE_PATH = "./data/aussie_low_q.jpg"

image = cv2.imread(IMAGE_PATH)

if image is None:
    print("Błąd: nie można wczytać obrazu!")
    exit()
else:
    print("Obraz wczytano poprawnie.")

cv2.imshow("Oryginalny obraz z cienkimi liniami", image)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

_, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))

thicknesses = []
iterations_range = range(1, 6)

for i in iterations_range:
    dilated = cv2.dilate(binary, kernel, iterations=i)
    cv2.imshow(f"Dylatacja - {i} iteracji", dilated)
    thickness = cv2.countNonZero(dilated)
    thicknesses.append(thickness)

cv2.waitKey(0)
cv2.destroyAllWindows()

plt.plot(list(iterations_range), thicknesses, marker="o")
plt.title("Wpływ liczby iteracji dylatacji na ilość białych pikseli")
plt.xlabel("Liczba iteracji")
plt.ylabel("Liczba białych pikseli")
plt.grid(True)
plt.show()
