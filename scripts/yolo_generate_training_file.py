import os

image_files = []
for filename in os.listdir("/home/primesh/darknet/data/obj/test/stain"):
    if filename.endswith(".jpg"):
        image_files.append("data/obj/test/stain/" + filename)
os.chdir("..")
with open("/home/primesh/darknet/data/test.txt", "a") as outfile:
    for image in image_files:
        outfile.write(image)
        outfile.write("\n")
    outfile.close()
os.chdir("..")