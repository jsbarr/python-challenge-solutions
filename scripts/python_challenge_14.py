#remember: 100*100 = (100+99+99+98) + (...
# Spiral our 1x10000 image into a 100x100 image

import os
import itertools
from PIL import Image

def get_spiral_coord_sequence(size, offset):
    # Returns the sequence of pixel co-ords obtained by starting at the top left corner of a size x size square whose
    # top left pixel is at position offset and performing a single clockwise spiral
    coord_seq = []
    current_pos = offset

    # Walk right
    coord_seq += [(current_pos[0] + i, current_pos[1]) for i in range(size)]
    current_pos = coord_seq[-1]

    # Walk down
    coord_seq += [(current_pos[0], current_pos[1] + i + 1) for i in range(size - 1)]
    current_pos = coord_seq[-1]

    # Walk left
    coord_seq += [(current_pos[0] - i - 1, current_pos[1]) for i in range(size - 1)]
    current_pos = coord_seq[-1]

    # Walk up
    coord_seq += [(current_pos[0], current_pos[1] - i - 1) for i in range(size - 2)]

    return coord_seq

image = Image.open(os.getcwd() + "\\..\\resources\\pc14_wire.png")
# Get RGB pixels
rgb_image = image.convert('RGB')
size = image.size # (10000,1)
raw_data_list = ["" for i in range(10000)]
positions = list(itertools.chain.from_iterable([get_spiral_coord_sequence(100 - (2*i) , (i,i)) for i in range(50)]))
# print(len(positions)) # 10000
for i in range(10000):
    original_pos = (i,0)
    r, g, b = rgb_image.getpixel(original_pos)
    new_pos = positions[i]
    new_pos_in_list = 100*new_pos[1] + new_pos[0]
    raw_data_list[new_pos_in_list] = chr(r) + chr(g) + chr(b) # Save this pixels data to position corresponding to the
    # pixel obtained from the positions list

raw_data = "".join(raw_data_list) # join into single string
output = Image.frombytes("RGB", (100,100), raw_data)
output.save(os.getcwd() + "\\..\\resources\\pc14_output.jpg")

# Picture of a cat ("and its name is Uzi. You'll hear from him later")