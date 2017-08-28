# 'Peak hell' = pickle
import urllib2
import pickle

response = urllib2.urlopen("http://www.pythonchallenge.com/pc/def/banner.p").read()

response_unpickled = pickle.loads(response) # List of lines of ascii art
for line in response_unpickled:
    line_string = ""
    for pair in line:
        line_string += pair[0]*pair[1]
    print(line_string)

# CHANNEL