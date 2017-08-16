import os
import sys
from PIL import Image

#https://stackoverflow.com/questions/1048658/resize-images-in-directory
def resize(folder, fileName, destination_folder, dim_width=17,dim_length=17):
    filePath = os.path.join(folder, fileName)
    im = Image.open(filePath)
    newIm = im.resize((dim_width,dim_length))
    new_target_path = os.path.join(destination_folder,fileName)
    # save the new image in a new directory
    newIm.save(new_target_path)

def bulkResize(imageFolder, destination_folder):
    imgExts = ["png", "bmp", "jpg"]
    for path, dirs, files in os.walk(imageFolder):
        for fileName in files:
            ext = fileName[-3:].lower()
            if ext not in imgExts:
                continue

            resize(path, fileName, destination_folder)


bulkResize('imgs','resized_imgs')