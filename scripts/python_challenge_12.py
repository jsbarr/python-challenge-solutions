# Dealing evil; evil2.jpg suggests changing file extension to GFX which appears to be some collection of images.  Cards
# in the picture have a sort of "5" on the back so try 'dealing' out 5 images

import os

image = open(os.getcwd() + "\\..\\resources\\pc12_evil2.gfx","rb").read()

for i in range(5):
    output_file = open(os.getcwd() + "\\..\\resources\\pc12_output{}.jpg".format(i),"wb")
    output_file.truncate()
    output_file.write(image[i::5])
    output_file.close()

# disproportional