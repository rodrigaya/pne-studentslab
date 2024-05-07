import http.client
import json
import socketserver
import termcolor
from pathlib import Path

SERVER = "rest.ensembl.org"
ENDPOINT = "/info/species"
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
# READ RESPONSE HTML AND REPLACE ANSWER
print(data1)

# Define the Server's port
PORT = 8080

# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True


# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inherits all his methods and propertie
class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        # Print the request line
        termcolor.cprint(self.requestline, 'green')
        print(self.requestline, 'green')

        # IN this simple server version:
        # We are NOT processing the client's request
        # It is a happy server: It always returns a message saying
        # that everything is ok
        folder = 'html/'
        search = self.requestline.split(' ')[1][1:].split('?')[0]
        print('Search: ' + search)
        try:
            if search == '':
                contents = Path(folder + 'index.html').read_text()
        except FileNotFoundError:
            contents = Path('html/error.html').read_text()

# -- Transform it into JSON format
# response = json.loads(data1)


# if response["ping"] == 1:
# -- Print the received data
# print(f"PING OK! The database is running")
