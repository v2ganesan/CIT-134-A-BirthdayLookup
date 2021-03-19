import json

with open('birthday.json') as jsonFile:
    dict = json.loads(jsonFile)

print(type(dict))