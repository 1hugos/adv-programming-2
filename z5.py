import cv2
import numpy as np

canvas = np.zeros((300, 300, 3), dtype="uint8")
center = (canvas.shape[1] // 2, canvas.shape[0] // 2)

for size in range(0, 200, 20):
    top_left = (center[0] - size // 2, center[1] - size // 2)
    bottom_right = (center[0] + size // 2, center[1] + size // 2)
    cv2.rectangle(canvas, top_left, bottom_right, (255, 255, 255), 1)

cv2.imshow("Eksperymentowanie", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()
