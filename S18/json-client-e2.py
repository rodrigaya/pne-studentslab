
import http.client
import json
from termcolor import cprint

PORT = 8080
SERVER = 'localhost'

print(f"\nConnecting to server: {SERVER}:{PORT}\n")

# Connect with the server
conn = http.client.HTTPConnection(SERVER, PORT)

# -- Send the request message, using the GET method. We are
# -- requesting the main page (/)
try:
    conn.request("GET", "/listusers")
except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()

# -- Read the response message from the server
r1 = conn.getresponse()

# -- Print the status line
print(f"Response received!: {r1.status} {r1.reason}\n")

# -- Read the response's body
data1 = r1.read().decode("utf-8")

# -- Create a variable with the data,
# -- form the JSON received
community = json.loads(data1)

print("CONTENT: ")

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
