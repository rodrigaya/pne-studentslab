import json
#import termcolor
from pathlib import Path

# -- Read the json file
jsonstring = Path("people-3.json").read_text()

# Create the object person from the json string
person = json.loads(jsonstring)

# Person is now a dictionary. We can read the values
# associated to the fields 'Firstname', 'Lastname' and 'age'

# Print the information on the console, in colors
print()
#termcolor.cprint("Name: ", 'green', end="")
print("Name: ", end="")
print(person['Firstname'], person['Lastname'])
#termcolor.cprint("Age: ", 'green', end="")
print("Age: ", end="")
print(person['age'])

# Get the phoneNumber list
phoneNumbers = person['phoneNumber']

# Print the number of elements in the list
#termcolor.cprint("Phone numbers: ", 'green', end='')
print("Phone numbers: ", end='')
print(len(phoneNumbers))

# Print all the numbers
for i, dictnum in enumerate(phoneNumbers):
    #termcolor.cprint("  Phone " + str(i + 1) + ": ", 'blue')
    print("  Phone " + str(i + 1) + ": ")

    # The element num contains 2 fields: number and type
    #termcolor.cprint("\t- Type: ", 'red', end='')
    print("\t- Type: ", end='')
    print(dictnum['type'])
    #termcolor.cprint("\t- Number: ", 'red', end='')
    print("\t- Number: ", end='')
    print(dictnum['number'])
