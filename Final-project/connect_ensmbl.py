import json
import http.client
import pprint

server = "rest.ensembl.org"
params = '?content-type=application/json'
#endpoint = '/info/assembly'
endpoint = '/info/species/'

# Connect with the server
conn = http.client.HTTPConnection(server)

# -- Send the request message, using the GET method. We are
# -- requesting the main page (/)
try:
    conn.request("GET", endpoint + params)
except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()

# -- Read the response message from the server
r1 = conn.getresponse()

# -- Print the status line
print(f"Response received!: {r1.status} {r1.reason}\n")

# -- Read the response's body
data1 = r1.read().decode("utf-8")
# READ RESPONSE HTML AND REPLACE ANSWER

# -- Transform it into JSON format
response = json.loads(data1)
# pprint.pp(response)

pprint.pp(response)
