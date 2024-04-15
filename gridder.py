import PIL
from PIL import Image
import os
import time
from random import randint
import math
import sys

def makeGrid(image_paths, gridSize):
    output_path = str(time.time()).split('.')[0] + ".jpg"
    images = [Image.open(path) for path in image_paths]

    '''total_height = ""
    max_height = ""
    max_width = ""
    '''
    #alttakini yaparsak eger en buyuk resme gore ayarliyor - kayip yok

    max_width = max(image.width for image in images)
    max_height = max(image.height for image in images)

    #the_width = 1000
    #the_height = 1000
    the_width = max_width
    the_height = max_height

    width_margin = 20
    height_margin = 50

    
    
    combined_image = Image.new('RGB', ((the_width+width_margin)*gridSize,(the_height+height_margin)*gridSize))

    cur_width=0
    cur_height=0
    cnt = 0

    
    for image in images:
        new_image = Image.new('RGB', (the_width, the_height))
        if(cnt < gridSize):
            new_image.paste(image, (0, 0))
            
            combined_image.paste(new_image, (cur_width, cur_height))
            cur_width += the_width
            cnt += 1
        else:
            new_image.paste(image, (0, 0))
            cur_height += the_height+height_margin
            combined_image.paste(new_image, (0, cur_height))
            cnt = 1
            cur_width = the_width

    combined_image.save(output_path)
    #delete_files(image_paths)
    print("Done...")

def delete_files(image_paths):
	for path in image_paths:
		os.remove(path)
		#print(f"File is deleted from {path}")
	print("[INFO] All files are deleted")


if __name__ == "__main__":
    directory = sys.argv[1]
    x = int(input("grid size?"))
    #x = sys.argv[1]
    all_files = os.listdir(directory)
    image_paths = []
    for files in all_files:
        image_paths.append(os.path.join(directory, files))
        
    makeGrid(image_paths,x)
