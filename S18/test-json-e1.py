import json
from termcolor import cprint
from pathlib import Path

# -- Read the json file
jsonstring = Path("people-e1.json").read_text()

# Create the object person from the json string
community = json.loads(jsonstring)

# Community is now a dictionary. We can read the values
# associated to the field 'people'

people = community['people']
print('Total people in the database: ' + str(len(people)))

for person in people:
    cprint('\nName: ', 'green', end='', force_color=True)
    print(person['Firstname'], person['Lastname'])
    cprint('Age: ', 'green', end='', force_color=True)
    print(person['age'])
    cprint('Phone numbers: ', 'green', end='', force_color=True)
    print(len(person['phoneNumber']))
    phoneNumbers = person['phoneNumber']

    for i, phone in enumerate(phoneNumbers, 1):
        cprint('  Phone: ', 'blue', end='', force_color=True)
        print(i)
        cprint('\tType: ', 'red', end='', force_color=True)
        print(phone['type'])
        cprint('\tNumber: ', 'red', end='', force_color=True)
        print(phone['number'])




