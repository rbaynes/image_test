#!/usr/bin/env python3.6

# https://pillow.readthedocs.io/en/3.1.x/reference/Image.html

# images/ACE4.png is 1280x1024 pixels, 96 DPI 

import os
from PIL import Image

def resize(input_file, output_file, size) -> None:
    try:
        im = Image.open(input_file)
        im.thumbnail(size, Image.ANTIALIAS)
        im.save(output_file, "PNG")
        print(f'Resized {input_file} to {output_file}')
    except Exception as e:
        print(f'Error {e}')
        
med_size = 640, 512
thumb_size = 128, 128

input_file = 'images/ACE4.png'
if_split = os.path.splitext(input_file)
med_file = if_split[0] + '_med' + if_split[1]
thumb_file = if_split[0] + '_thumb' + if_split[1]

resize(input_file, med_file, med_size)
resize(input_file, thumb_file, thumb_size)
