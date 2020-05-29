import numpy as np
import cv2

img = cv2.imread('test2.jpg',0)

# create a CLAHE object (Arguments are optional).
clahe = cv2.createCLAHE(clipLimit=4.0, tileGridSize=(8,8))
cl1 = clahe.apply(img)

cv2.imwrite('eq_test2_adaptive_4.jpg',cl1)