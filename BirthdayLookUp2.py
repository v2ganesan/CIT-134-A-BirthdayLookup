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


while True:
    search = str(input("Enter a name: "))

    birthdays = []
    if search != "Exit":
        for key in birthdayDictionary.keys():
            if search in key:
                print(key)
                birthdays.append(birthdayDictionary[key])
        print(birthdays)
    else:
        break

