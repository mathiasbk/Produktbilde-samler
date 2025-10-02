import os
import shutil

ProductImagePath = input("Enter source folder, containtn subfolders: ")

ImageOutputPath = input("Enter output path: ")

RawProductnumbers = input("Enter productnumbers. Comma sepparated: ")

productnumbers = RawProductnumbers.split(",")

print(f"Productnumbers. {productnumbers}")

# Iterate over input folder and list only folder names
for root, dirnames, filenames in os.walk(ProductImagePath):
    for folder_name in dirnames:
        #print(f"Found folder: {folder_name}")
        if(folder_name in productnumbers):
            #Folder found
            print(f"Found folder {folder_name}.")
            source_path = os.path.join(root, folder_name)
            destination_path = os.path.join(ImageOutputPath, folder_name)
            shutil.copytree(source_path, destination_path)