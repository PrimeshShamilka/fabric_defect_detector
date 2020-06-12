import os

source_dir = '/media/primesh/F4D0EA80D0EA4906/PROJECTS/Automation_challenge3/Datasets/FabricDefectDetector_datasets/dataset7/test/defect_free'
target_dir = source_dir

for f in os.listdir(source_dir):
    if f.endswith('.jpg'):
        open(os.path.join(target_dir, f.replace('.jpg', '.txt')), 'w+').close()