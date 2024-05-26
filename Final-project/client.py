import http.client
import http.server
import json
from termcolor import cprint
import pprint


def client(endpoint, params=None):
    PORT = 8080
    SERVER = 'localhost'

    print(f"\nConnecting to server: {SERVER}:{PORT}\n")

    # Connect with the server
    conn = http.client.HTTPConnection(SERVER, PORT)

    # -- Send the request message, using the GET method. We are
    # -- requesting the main page (/)
    try:
        conn.request("GET", endpoint + '?' + params + '&' + 'json=1')
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
    response = json.loads(data1)
    return response


client('/listSpecies', 'limit=1')

