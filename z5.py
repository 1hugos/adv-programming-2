import cv2

img1 = cv2.imread("./data/dog.jpg")
img2 = cv2.imread("./data/dog_grey.jpg")

resized_img_1 = cv2.resize(img1, (1024, 768))
resized_img_2 = cv2.resize(img2, (1024, 768))

cv2.imshow("Pies", resized_img_1)
cv2.imshow("Szary pies", resized_img_2)

while True:
    key = cv2.waitKey(0)

    if cv2.getWindowProperty("Pies", cv2.WND_PROP_VISIBLE) < 1:
        cv2.destroyWindow("Pies")

    if cv2.getWindowProperty("Szary pies", cv2.WND_PROP_VISIBLE) < 1:
        cv2.destroyWindow("Szary pies")

    if cv2.getWindowProperty("Pies", cv2.WND_PROP_VISIBLE) < 1 and \
       cv2.getWindowProperty("Szary pies", cv2.WND_PROP_VISIBLE) < 1:
        break

cv2.destroyAllWindows()
