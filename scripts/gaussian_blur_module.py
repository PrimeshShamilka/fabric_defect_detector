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

def apply_gaussian_blur(img):
    blur = cv2.GaussianBlur(img,(5,5),0)
    return blur


# source_dir = '/media/primesh/F4D0EA80D0EA4906/PROJECTS/Automation_challenge3/preprocessing/images/histogram_equalized'
# target_dir = '/media/primesh/F4D0EA80D0EA4906/PROJECTS/Automation_challenge3/preprocessing/images/h_equa_plus_gauss_blur'

# source_dir = '/home/primesh/darknet/data/obj_preprocessed/train/stain'
source_dir = '/home/primesh/Desktop/a'
target_dir = source_dir

for filename in os.listdir(source_dir):
    if filename.endswith('.jpeg'):
        img = cv2.imread(os.path.join(source_dir,filename),0)
        if img is not None:
            blur_image = apply_gaussian_blur(img)
            target_path = os.path.join(target_dir, filename)
            cv2.imwrite(target_path, blur_image)