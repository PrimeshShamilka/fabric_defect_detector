import os
for f in os.listdir(source_dir):
    if f.endswith('.jpg'):
        open(os.path.join(target_dir, f.replace('.jpg', '.txt')), 'w+').close()