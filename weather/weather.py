import sys
import os
from json import dumps
from xmljson import yahoo  as yahoo
import xml.etree.ElementTree as ET

if(len(sys.argv)!=2) :              #if there are more 1 argument
    print("Wrong Path")
    exit()
if(os.path.isfile(sys.argv[1])) :   #if file exits
    file = open(sys.argv[1],"r")
else :
    print("File isn't exist")
    exit()
xmlFile = ET.parse(file).getroot()
coverted = dumps(yahoo.data(xmlFile)["current"], indent=4)  #Convert to json with current root and indent = 4
newFilename = sys.argv[1].split(".")[0]                     #Get xml file name
convertedFile = open(newFilename + ".json", "w")
convertedFile.write(coverted)                               #write json into file
convertedFile.close()
file.close()
print(newFilename + ".json")