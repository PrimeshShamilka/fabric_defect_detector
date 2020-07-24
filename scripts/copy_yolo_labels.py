# copy labels of images from one folder to another folder 
# input --> image names

import os
import shutil

img_folder = '/media/primesh/F4D0EA80D0EA4906/PROJECTS/Automation_challenge3/Datasets/kaggle_fabric_stain_defect_dataset/images/stain'
label_file_folder = '/media/primesh/F4D0EA80D0EA4906/PROJECTS/Automation_challenge3/Datasets/FabricDefectDetector_datasets/dataset5_2/images/stain_labels'

img_names = os.listdir(img_folder)
for img_name in img_names:
    lbl_file_name = img_name.split('.')[0] + '.txt'
    lbl_file_path = label_file_folder + '/' + lbl_file_name
    shutil.copy(lbl_file_path, img_folder)
