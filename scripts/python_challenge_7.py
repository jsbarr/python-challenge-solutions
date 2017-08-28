# smarty
import png
import os
reader = png.Reader(file = open(os.getcwd() + "\\..\\resources\\pc7_oxygen.png", "rb"))

data = reader.read()
pixels = data[2]

row = list(pixels)[50]
width = len(row) / 4
output = ""


for i in range(width):
    pixel = row[(4 * i):(4* (i + 1))] # R G B alpha

    output += chr(pixel[0])

print(output)

# (After dedupe): "smart guy, you made it. the next level is [105,110,116,101,103,114,105,116,121]"

codes = [105,110,116,101,103,114,105,116,121]
output = ""
for code in codes:
    output += chr(code)
print output

# INTEGRITY