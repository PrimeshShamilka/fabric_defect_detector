import os
import numpy as np
import shutil

# # Creating Train / Val / Test folders (One time use)
root_dir = os.path.dirname(os.path.realpath(__file__))
pos_cls = 'stain'
neg_cls = 'defect_free'

os.makedirs(root_dir +'/train/' + pos_cls)
os.makedirs(root_dir +'/train/' + neg_cls)
os.makedirs(root_dir +'/valid/' + pos_cls)
os.makedirs(root_dir +'/valid/' + neg_cls)
os.makedirs(root_dir +'/test/' + pos_cls)
os.makedirs(root_dir +'/test/' + neg_cls)

# Creating partitions of the data after shuffeling
current_cls = pos_cls
src = root_dir + "/images/" + current_cls # Folder to copy images from

print (src)
all_file_name = os.listdir(src)
np.random.shuffle(all_file_name)
train_file_names, valid_file_names, test_file_names = np.split(np.array(all_file_name),
                                                          [int(len(all_file_name)*0.7), int(len(all_file_name)*0.85)])


train_file_names = [src+'/'+ name for name in train_file_names.tolist()]
valid_file_names = [src+'/' + name for name in valid_file_names.tolist()]
test_file_names = [src+'/' + name for name in test_file_names.tolist()]

print('Total images: ', len(all_file_name))
print('Training: ', len(train_file_names))
print('Validation: ', len(valid_file_names))
print('Testing: ', len(test_file_names))

train_dest_dir = root_dir + '/train/' + current_cls
valid_dest_dir = root_dir + '/valid/' + current_cls
test_dest_dir = root_dir + '/test/' + current_cls

# Copy-pasting images
for name in train_file_names:
    shutil.copy(name, train_dest_dir)

for name in valid_file_names:
    shutil.copy(name, valid_dest_dir)

for name in test_file_names:
    shutil.copy(name, test_dest_dir)

