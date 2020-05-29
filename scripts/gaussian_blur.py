import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('/media/primesh/F4D0EA80D0EA4906/PROJECTS/Automation_challenge3/preprocessing/images/histogram_equalized/1.jpg')
blur = cv.GaussianBlur(img,(5,5),0)
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur),plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.show()