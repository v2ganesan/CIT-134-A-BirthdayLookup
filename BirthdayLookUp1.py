import json

try:
    jsonFile = open('birthday.json', 'r')
except OSError:
    print("ERROR: Unable to open the file.")

birthdayList = json.load(jsonFile)
birthdayDictionary = {} 

#creates empty dictionary to put values into 
for elem in birthdayList:
    name = elem["name"]
    birthday = elem["birthday"]

    birthdayDictionary[name] = birthday

name = input("Enter a name: ")
print("Name: " + name)


if name in birthdayDictionary.keys():
    print("Birthday: " + birthdayDictionary[name])
else:
    print("ERROR!")