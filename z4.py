import cv2
import numpy as np

canvas = np.zeros((300, 300, 3), dtype="uint8")

center = (150, 150)

cv2.rectangle(canvas, (100, 100), (200, 200), (255, 255, 255), 2)

cv2.circle(canvas, center, 30, (255, 255, 255), 2)

cv2.imshow("Złożona figura", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()