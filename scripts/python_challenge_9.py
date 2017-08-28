# Connect the dots

import time
import os
import sys

from PIL import Image
from PIL import ImageDraw

image = Image.open(os.getcwd() + "\\..\\resources\\pc9_good.jpg")

draw = ImageDraw.Draw(image)
draw.line((0, 0) + image.size, fill = (0,0,0))
draw.line((0, image.size[1], image.size[0],0), fill = (0,0,0))

del draw

image.show()
time.sleep(60)

image.save(sys.stdout, "JPEG")