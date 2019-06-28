#!/usr/bin/env python3.6

# https://pillow.readthedocs.io/en/3.1.x/reference/Image.html

# images/ACE4.png is 1280x1024 pixels, 96 DPI 

import os
from PIL import Image

def resize(input_file, output_file, size=None) -> None:
    try:
        img = Image.open(input_file)
        if size is None:
            # halves each dimension 
            size = int(img.size[0] / 2), int(img.size[1] / 2)
        print(f'Resized {img.size} {input_file} to {size} {output_file}')
        img.thumbnail(size, Image.ANTIALIAS)
        img.save(output_file)  #, "PNG")
    except Exception as e:
        print(f'Error {e}')
        
input_file = 'images/ACE4.png'
if_split = os.path.splitext(input_file)
med_file = if_split[0] + '_med' + if_split[1]
thumb_file = if_split[0] + '_thumb' + if_split[1]

resize(input_file, med_file) 
resize(input_file, thumb_file, (128, 128))
