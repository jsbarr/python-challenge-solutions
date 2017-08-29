# straighten up

import os
import itertools
from PIL import Image



image = Image.open(os.getcwd() + "\\..\\resources\\pc16_mozart.gif")
# Get RGB pixels
rgb_image = image.convert('RGB')
size = image.size # (640,480)
positions = [tuple(reversed(pair)) for pair in itertools.product(range(size[1]), range(size[0]))]

"""
Testing - used to identify the repeated pink sections.  These correspond to 5 pixels of (R, G, B)=(255, 0, 255)
current_rgb = (0,0,0)
for pos in positions:
    next_rgb = rgb_image.getpixel(pos)
    if next_rgb == current_rgb:
        print(next_rgb, pos)
    current_rgb = next_rgb
"""

rgb_string = ""
for pos in positions:
    r, g, b = rgb_image.getpixel(pos)
    rgb_string += chr(r) + chr(g) + chr(b)

# Split string on the pink bands
lines = rgb_string.split(( chr(255) + chr(0) + chr(255) )*5)
max_length = max([len(line) for line in lines])
num_lines = len(lines)

rgb_string = ""
for line in lines:
    rgb_string += line + (chr(0) * (max_length - len(line))) # append black pixels to make lines same length


output = Image.frombytes("RGB", (max_length/3, num_lines), rgb_string)
output.save(os.getcwd() + "\\..\\resources\\pc16_output.gif")

# output image contains the word 'romance'