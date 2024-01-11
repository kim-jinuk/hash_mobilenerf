import sys
import os
from PIL import Image

data_name = sys.argv[1]

print("Generate resized image.")

if not os.path.exists('datasets/nerf_llff_data/' + data_name + '/images_4'):
    images = os.listdir('datasets/nerf_llff_data/' + data_name + '/images')
    os.makedirs('datasets/nerf_llff_data/' + data_name + '/images_4')

    for image in images:
        img = Image.open('datasets/nerf_llff_data/' + data_name + '/images/' + image)
        a = img.resize((int(img.size[0]/4), int(img.size[1]/4)))
        a.save('datasets/nerf_llff_data/' + data_name + '/images_4/' + image)
    
print("Done.")