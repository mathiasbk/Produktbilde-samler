import os
import shutil
from tqdm import tqdm
import csv


ProductImagePath = input("Enter source folder, containing subfolders: ")
ImageOutputPath = input("Enter output path: ")
RawProductnumbers = input(
    "Enter product numbers. Leave empty if you want to provide a text file. "
    "Comma separated: "
)

def get_missing_products(productnumbers, foundproductnumbers):
    return [
        productnumber
        for productnumber in productnumbers
        if productnumber not in foundproductnumbers
    ]



#CSV data
csvdata = [
    ['Produktnumber', 'Found', 'Found Count'],
]

if RawProductnumbers == "":
    ProductnumbersFile = input("Enter path to text file with product numbers: ")

    with open(ProductnumbersFile, "r") as f:
        productnumbers = [line.strip() for line in f if line.strip()]
else:
    productnumbers = [
        number.strip()
        for number in RawProductnumbers.split(",")
    ]

# Remove duplicate product numbers
productnumbers = list(set(productnumbers))

foundproductnumbers = []

print(f"Looking for {len(productnumbers)} product numbers...")

for root, dirnames, filenames in os.walk(ProductImagePath):

    for folder_name in dirnames:

        if folder_name in productnumbers:
            # Folder found
            foundproductnumbers.append(folder_name)

            source_path = os.path.join(root, folder_name)
            destination_path = os.path.join(
                ImageOutputPath,
                folder_name
            )

            #Add to CSV report
            csvdata.append([
                folder_name,
                "Yes",
                len(os.listdir(source_path))
            ])
            try:
                shutil.copytree(
                    source_path,
                    destination_path
                )
            except Exception as e:
                print(f"Error copying folder {folder_name}. "        "The folder may already exist in the destination.")


    # Break if we have found all images we are looking for
    if len(foundproductnumbers) == len(productnumbers):
        break

# Add products that were not found
missingproductnumbers = get_missing_products(productnumbers, foundproductnumbers)
for productnumber in missingproductnumbers:
    csvdata.append([
        productnumber,
        "No",
        0
    ])

# Write CSV report
with open(os.path.join(ImageOutputPath, "report.csv"), "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(csvdata)


print()
print("Done copying folders.")

quit = input("Press any key to exit.")
