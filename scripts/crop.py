import numpy as np
import cv2
import glob
import matplotlib.pyplot as plt


# Cropping 512x512 images to 128x128
src_folder = '/media/primesh/F4D0EA80D0EA4906/ACADEMICS/MORA/Sem 5/Automation challenge 3/Fabric defect detector/Binary classifier for defect detection/Dataset1/Test' # folder to read images from
dst_folder = '/media/primesh/F4D0EA80D0EA4906/ACADEMICS/MORA/Sem 5/Automation challenge 3/Fabric defect detector/Binary classifier for defect detection/Dataset1/TestCropped' # folder to save cropped images to
classes = ['Defect','NoDefect']

for i, class_name in enumerate(classes):
    string = src_folder + '/'+ class_name + '/*.tif'
    string_list = glob.glob(string)
    class_list = [cv2.imread(img) for img in string_list] # read images
    print(len(class_list))
    plt.imshow(class_list[0])
    for j, img in enumerate(class_list):
        n = 128 # window length
        s = img.shape[0]/n # number of tiles along length
        tiles = [np.hsplit(i, s) for i in np.vsplit(img, s)] # tiling
        flat = [item for sublist in tiles for item in sublist] # flattening the list
        dst_loc = dst_folder + '/'+ class_name + '/' # subfolders to save images in
        print(dst_loc)
        for t, tile in enumerate(flat):
            fname = dst_loc + str(j) + '_' + str(t) + '.jpg' #save location with filename
            cv2.imwrite(fname, tile) # saving