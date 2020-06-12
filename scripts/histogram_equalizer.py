import cv2
import numpy as np
import os

def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        if filename.endswith('.jpg'):
            img = cv2.imread(os.path.join(folder,filename),0)
            if img is not None:
                images.append(img)
    return images

def histogram_equilize(img):
    equ = cv2.equalizeHist(img)
    return equ

def contrast_limited_adaptive_histogram_equalization(img):
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    cl1 = clahe.apply(img)
    return cl1  

# img = cv2.imread('test6.jpg',0)
# print (img)
# equ = cv2.equalizeHist(img)
# res = np.hstack((img,equ)) #stacking images side-by-side
# cv2.imwrite('res.png',equ)

# source_dir = '/home/primesh/darknet/data/obj_preprocessed/train/stain'
source_dir = '/home/primesh/Desktop/a'
target_dir = source_dir
# target_dir = '/home/primesh/darknet/data/obj/valid/stain'

# source_dir = '/media/primesh/F4D0EA80D0EA4906/PROJECTS/Automation_challenge3/preprocessing/images/raw'
# target_dir = '/media/primesh/F4D0EA80D0EA4906/PROJECTS/Automation_challenge3/preprocessing/images/histogram_equalized'

for filename in os.listdir(source_dir):
    if filename.endswith('.jpg'):
        img = cv2.imread(os.path.join(source_dir,filename),0)
        if img is not None:
            # equ = histogram_equilize(img)
            clahe = contrast_limited_adaptive_histogram_equalization(img)    
            target_path = os.path.join(target_dir, filename)
            cv2.imwrite(target_path, clahe)