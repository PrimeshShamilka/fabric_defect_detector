import os

label_file_folder = '/media/primesh/F4D0EA80D0EA4906/PROJECTS/Automation_challenge3/Datasets/FabricDefectDetector_datasets/dataset5/images/stain_labels'
stain_dims_file_path = '/media/primesh/F4D0EA80D0EA4906/PROJECTS/Automation_challenge3/Datasets/FabricDefectDetector_datasets/dataset5/images/stain_dims.csv'
stain_dims= []

label_files = os.listdir(label_file_folder)
print (label_files)

stain_dims_file = open(stain_dims_file_path, 'w', encoding = 'utf-8')
stain_dims_file.write("width, height\n")
stain_dims_file.close()


for label_file_name in label_files:
    label_file = open((label_file_folder + '/' + label_file_name))
    lines = label_file.readlines()
    for line in lines:
        label = line.rstrip().split(' ')
        stain_dim = [int(float(label[2])*256), int(float(label[3])*256)]
        stain_dims.append(stain_dim)

        stain_dim_s = ""
        stain_dim_s += str(stain_dim[0]) + ',' + str(stain_dim[1]) + '\n'

        stain_dims_file = open(stain_dims_file_path, 'a', encoding = 'utf-8')
        stain_dims_file.write(stain_dim_s)
        stain_dims_file.close()

        print(stain_dim)