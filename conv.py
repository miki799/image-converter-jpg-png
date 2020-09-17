import sys
import os
from PIL import Image

'''
JP(E)G <--> PNG converter
Folder names must be passed as arguments.
First argument -> directory with images to be converted
Second argument -> directory with converted images
Example:
...> python conv.py 'example_images\' 'new\' 
'''


def converter(image_folder, output_folder):
    # creates folder
    if not os.path.exists(output_folder):
        os.mkdir(output_folder)
    # converts
    for file_name in os.listdir(image_folder):
        name, ext = os.path.splitext(file_name)
        print(name, ext)
        # checks file format
        if (ext == '.jpg') or (ext == '.jpeg'):
            print(f'Converting {file_name} to .png format...')
            converted = name + '.png'
        elif ext == '.png':
            print(f'Converting {file_name} to .jpg format...')
            converted = name + '.jpg'
        # saves converted image in output folder
        with Image.open(image_folder + file_name) as img:
            img.save(output_folder + converted)


converter(sys.argv[1], sys.argv[2])
