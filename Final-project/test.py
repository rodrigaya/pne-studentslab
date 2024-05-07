import http.server
import socketserver
import termcolor
from pathlib import Path
import http.client
import json


def get_contents(search):
    server = "rest.ensembl.org"
    if search == '1':
        endpoint = '/info/species'
        params = '?content-type=application/json'
    else:
        endpoint = '/info/assembly/homo_sapiens'
        params = '?content-type=application/json'

    url = server + endpoint + params

    print(f"\nServer: {server}")
    print(f"URL: {url}")

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
    print(data1)

    # -- Transform it into JSON format
    response = json.loads(data1)
    return data1


# Define the Server's port
PORT = 8080

# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True


# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inherits all his methods and properties
class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        # Print the request line
        termcolor.cprint(self.requestline, 'green')

        folder = 'html/'
        search = self.requestline.split(' ')[1][1:].split('?')[0]
        msg = self.requestline.split('msg=')[1].split(' ')[0]
        print(msg)
        print('Search: ' + search)
        try:
            if search == '':
                contents = Path(folder + 'main.html').read_text()
            elif search == '1':
                if not msg.isdigit():
                    contents = Path('html/error.html').read_text().replace('Resource not available',
                                                                           'Only numbers allowed')
                else:
                    contents = Path(folder + 'content.html').read_text().replace('{content}', get_contents(search))
            # elif search == 2:
            # elif search == 3:
        except FileNotFoundError:
            contents = Path('html/error.html').read_text()

        # Generating the response message
        self.send_response(200)  # -- Status line: OK!

        # Define the content-type header:
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(contents)))

        # The header is finished
        self.end_headers()

        # Send the response message
        self.wfile.write(str.encode(contents))

        return


# ------------------------
# - Server MAIN program
# ------------------------
# -- Set the new handler
Handler = TestHandler

# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at PORT", PORT)

    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stopped by the user")
        httpd.server_close()
