# Phone that evil - accessing http://www.pythonchallenge.com/pc/phonebook.php gives an XML error, which is
# traceable to an improper call to a php page serving XML RPC (need to pass in a carefully structured  POST request)

import xmlrpclib

s = xmlrpclib.ServerProxy('http://www.pythonchallenge.com/pc/phonebook.php')
print(s.system.listMethods()) # ['phone', 'system.listMethods', 'system.methodHelp', 'system.methodSignature', 'system.multicall', 'system.getCapabilities']

print(s.phone("evil")) # He is not the evil -> "phone THAT evil?"
print(s.system.methodHelp("phone")) # Returns the phone of a person

# Saving "evil4.jpg" from previous challenge (despite being told at evil3 that there are no more evils...) we are told
# "Bert is evil! Go back!"

print(s.phone("Bert"))
# 555-ITALY

#italy