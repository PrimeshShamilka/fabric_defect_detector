# copy set of images from a src_img_folder to dst_img_folder
# input --> image names in img_names_folder

import os
import shutil

img_names_folder = '/media/primesh/F4D0EA80D0EA4906/PROJECTS/Automation_challenge3/Datasets/FabricDefectDetector_datasets/dataset5_2/images/stain'
dst_img_folder = '/media/primesh/F4D0EA80D0EA4906/PROJECTS/Automation_challenge3/Datasets/FabricDefectDetector_datasets/dataset5_2/images_raw/stain'
src_img_folder = '/media/primesh/F4D0EA80D0EA4906/PROJECTS/Automation_challenge3/Datasets/huaweiGR5_images/cropped'

img_names = os.listdir(img_names_folder)
for img_name in img_names:
    dst_img_file_path = src_img_folder + '/' + img_name
    shutil.copy(dst_img_file_path, dst_img_folder)
