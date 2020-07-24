import os 
dir_path = os.path.dirname(os.path.realpath(__file__)) + '/images2_video'

for count, filename in enumerate(os.listdir(dir_path)): 
    name ="fabric" + str(count+1) + ".jpg"
    src = dir_path + '/' + filename 
    dst = dir_path +  '/' + name 
        
    # rename() function will 
    # rename all the files 
    os.rename(src, dst) 