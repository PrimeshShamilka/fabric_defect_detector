import cv2
import numpy as np
from matplotlib import pyplot as plt
import os

def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        if filename.endswith('.jpg'):
            img = cv2.imread(os.path.join(folder,filename),0)
            if img is not None:
                images.append(img)
    return images

def generate_histogram(img):
    hist,bins = np.histogram(img.flatten(),256,[0,256])
    cdf = hist.cumsum()
    cdf_normalized = cdf * hist.max()/ cdf.max()
    return cdf_normalized

source_dir = '/media/primesh/F4D0EA80D0EA4906/PROJECTS/Automation_challenge3/preprocessing/images/h_equa_plus_gauss_blur_images'
target_dir = '/media/primesh/F4D0EA80D0EA4906/PROJECTS/Automation_challenge3/preprocessing/images/histograms_after_h_equa_plus_gauss'

# source_dir = '/home/primesh/darknet/data/obj_h_equa_plus_gauss_blur/valid/stain'
# target_dir = source_dir

for filename in os.listdir(source_dir):
    if filename.endswith('.jpg'):
        img = cv2.imread(os.path.join(source_dir,filename),0)
        if img is not None:
            histogram = generate_histogram(img)
            target_path = os.path.join(target_dir, filename)
            # cv2.imwrite(target_path, histogram)
            plt.plot(histogram, color = 'b')
            plt.hist(img.flatten(),256,[0,256], color = 'r')
            plt.xlim([0,256])
            plt.legend(('cdf','histogram'), loc = 'upper left')
            plt.savefig(target_path)
            plt.clf()