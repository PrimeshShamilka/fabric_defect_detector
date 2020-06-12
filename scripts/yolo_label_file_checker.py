import os
root_dir = os.path.dirname(os.path.realpath(__file__))

img_folder = root_dir + '/stain'
label_file_folder = root_dir + '/b'

image_names = os.listdir(img_folder)
label_file_names = os.listdir(label_file_folder)

image_names.sort()
label_file_names.sort()

miss_count = 0
count = 0

for image_name in image_names:    
    if image_name.split('.')[0] != label_file_names[count].split('.')[0]:
        miss_count+=1
    count+=1

print (miss_count)