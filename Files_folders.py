import os

# Specify the path to count files and folders
PATH = r'C:\Users\MD ZOBAIR AHMED\Desktop\Python_smale_code'

files = 0
folders = 0

for root, foldernames, filenames in os.walk(PATH):
    files += len(filenames)
    folders += len(foldernames)

print('Files:', files)
print('folders:', folders)
print('Total:', files + folders)