import sys
import os
import json
from xmltodict
#from xmljson import parker as pk
#from json import dumps

print(sys.argv)
if(len(sys.argv)!=2) :
    print("Wrong Path")
    exit()
if(os.path.isfile(sys.argv[1])) :
    file = open(sys.argv[1],"r")
else :
    print("File isn't exist")
    exit()
x = xmltodict.parse(file)
#print(dumps(pk.data(file)))