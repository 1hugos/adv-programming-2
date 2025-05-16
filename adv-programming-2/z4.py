import cv2

IMAGE_PATH = "./data/dog.jpg"
OUTPUT_PATH = "./data/dog_grey.jpg"

image_grey = cv2.imread(IMAGE_PATH, cv2.IMREAD_GRAYSCALE)

if image_grey is None:
    print("Błąd: nie można wczytać obrazu!")
else:
    print("Obraz wczytano poprawnie.")

    success = cv2.imwrite(OUTPUT_PATH, image_grey)
    
    if success:
        print(f"Obraz zapisano jako {OUTPUT_PATH}")
    else:
        print("Błąd przy zapisie obrazu.")
