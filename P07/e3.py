import http.client
import json
from termcolor import cprint

genes = {
    'FRAT1': 'ENSG00000165879',
    'ADA': 'ENSG00000196839',
    'FXN': 'ENSG00000165060',
    'RNU6_269P': 'ENSG00000212379',
    'MIR633': 'ENSG00000207552',
    'TTTY4C': 'ENSG00000228296',
    'RBMY2YP': 'ENSG00000227633',
    'FGFR3': 'ENSG00000068078',
    'KDR': 'ENSG00000128052',
    'ANK2': 'ENSG00000145362'
}

idg = genes['MIR633']

SERVER = "rest.ensembl.org"
ENDPOINT = "/sequence/id/" + idg
PARAMS = "?content-type=application/json"

URL = SERVER + ENDPOINT + PARAMS

print(f"\nServer: {SERVER}")
print(f"URL: {URL}")

# Connect with the server
conn = http.client.HTTPConnection(SERVER)

# -- Send the request message, using the GET method. We are
# -- requesting the main page (/)
try:
    conn.request("GET", ENDPOINT + PARAMS)
except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()

# -- Read the response message from the server
r1 = conn.getresponse()

# -- Print the status line
print(f"Response received!: {r1.status} {r1.reason}\n")

# -- Read the response's body
data1 = r1.read().decode("utf-8")

# -- Transform it into JSON format
response = json.loads(data1)

cprint('Gene: ', 'yellow', end='', force_color=True)
print('MIR633')
cprint('Description: ', 'yellow', end='', force_color=True)
print(response['desc'])
cprint('Bases: ', 'yellow', end='', force_color=True)
print(response['seq'])
