import cv2
import numpy as np

canvas = np.zeros((300, 300), dtype="uint8")

triangle_cnt = np.array([[150, 50], [50, 250], [250, 250]])
triangle = np.zeros_like(canvas)
cv2.drawContours(triangle, [triangle_cnt], 0, 255, -1)

circle = np.zeros_like(canvas)
cv2.circle(circle, (150, 150), 100, 255, -1)

bitwise_and = cv2.bitwise_and(triangle, circle)
bitwise_or = cv2.bitwise_or(triangle, circle)
bitwise_xor = cv2.bitwise_xor(triangle, circle)
bitwise_not = cv2.bitwise_not(triangle)

cv2.imshow("Triangle", triangle)
cv2.imshow("Circle", circle)
cv2.imshow("AND", bitwise_and)
cv2.imshow("OR", bitwise_or)
cv2.imshow("XOR", bitwise_xor)
cv2.imshow("NOT Triangle", bitwise_not)
cv2.waitKey(0)
cv2.destroyAllWindows()
