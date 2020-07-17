import os
import numpy as np

# root_dir should include test, train, valid folders (each folder having all the classes as folders)
# test.txt, train.txt, valid.txt files will be saved into dst_dir

root_dir = '/media/primesh/F4D0EA80D0EA4906/PROJECTS/Automation_challenge3/Datasets/FabricDefectDetector_datasets/dataset5_2'
dst_dir = root_dir

folder = 'train'
dst_file = dst_dir + '/' + folder + '.txt'
classes = ['stain','defect_free']


image_files = []

for class_name in classes:
    img_dir = root_dir + '/' + folder + '/' + class_name
    relative_dir = 'data/obj/' + folder + '/' + class_name
    for filename in os.listdir(img_dir):
        if filename.endswith(".jpg"):
            image_files.append(relative_dir + '/' + filename)
        if filename.endswith(".JPG"):
            image_files.append(relative_dir + '/' + filename)        
os.chdir("..")

np.random.shuffle(image_files)

with open(dst_file, "w") as outfile:
    for image in image_files:
        outfile.write(image)
        outfile.write("\n")
    outfile.close()
os.chdir("..")