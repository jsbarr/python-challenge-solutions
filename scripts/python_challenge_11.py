# Odd even - possibly two interlaced images?

import os
import itertools
from PIL import Image

image = Image.open(os.getcwd() + "\\..\\resources\\pc11_cave.jpg")
# Get RGB pixels
rgb_image = image.convert('RGB')
size = image.size
raw_data = ""
positions = [tuple(reversed(pair)) for pair in itertools.product(range(size[1]), range(size[0]))]
for pos in positions:
    if pos[0] * pos[1] % 2 == 0: continue # skip evens
    r, g, b = rgb_image.getpixel(pos)
    raw_data += chr(r) + chr(g) + chr(b)
output = Image.frombytes("RGB", (size[0]/2, size[1]), raw_data)
output.save(os.getcwd() + "\\..\\resources\\pc11_cave_output.jpg")

# Output file contains text "evil"