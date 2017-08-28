import os
import zipfile

# This code followed the text files to receive "collect the comments." Need to use python ZIP libraries to extract
# the archive comments for each file as we go, see below

"""
def read_next_nothing(current_nothing):
    cwd = os.getcwd() # .../challenges/scripts
    abs_path = cwd + "\\..\\resources\\pc6_channel\\{}.txt".format(current_nothing)
    with open(abs_path, 'r') as file:
        line = file.read()
        print(line)
        next_nothing = line.split(" ")[-1]
    return next_nothing

current_nothing = "90052"
for i in range(4000):
    current_nothing = read_next_nothing(current_nothing)
"""

def read_next_nothing(current_nothing, archive):
    current_file = "{}.txt".format(current_nothing)
    line = archive.open(current_file, "r").read()
    comment = archive.getinfo(current_file).comment
    return line.split(" ")[-1], comment


cwd = os.getcwd() # ...\\challenges\\scripts
abs_path = cwd + "\\..\\resources\\pc6_channel.zip"
archive = zipfile.ZipFile(abs_path)
comments = ""
current_nothing = "90052"
for i in range(4000):
    try:
        current_nothing, comment = read_next_nothing(current_nothing, archive)
    except KeyError:
        break
    comments += comment

print(comments)

# HOCKEY -> "It's in the air - look at the letters"
# Letter constituents spell OXYGEN