# # Exercise - 7... Question... Clean the Clutter... 



# Write a program to clean the clutter inside a folder on your computer. You should use os MOdule to rename all the png images from 1.png all the way till n.png where n is the number of png files in that folder. Do the same for other file formats... not only for png format







import os

folder_path = r"C:\Users\ACER\OneDrive\Desktop\OS Module Introduction Day46"

folders = os.listdir(folder_path)

count = {}

for folder in folders:

    old_path = os.path.join(folder_path, folder)

    if os.path.isdir(old_path):

        name, extension = os.path.splitext(folder)

        if extension not in count:
            count[extension] = 0

        count[extension] += 1

        new_name = str(count[extension]) + extension

        new_path = os.path.join(folder_path, new_name)

        os.rename(old_path, new_path)

print("Renaming Completed!")