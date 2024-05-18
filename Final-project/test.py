import http.server
import socketserver
from termcolor import cprint
from pathlib import Path
import http.client
import json
import pprint

server = "rest.ensembl.org"


def get_ep(search, name=None):
    params = '?content-type=application/json'
    if search == 'listSpecies':
        endpoint = '/info/species'
    else:
        endpoint = '/info/assembly' + name

    return endpoint + params


def get_info(ep):
    # Connect with the server
    conn = http.client.HTTPConnection(server)

    # -- Send the request message, using the GET method. We are
    # -- requesting the main page (/)
    try:
        conn.request("GET", ep)
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
    # pprint.pp(response)
    return response


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

        folder = 'html/'

        # Print the request line
        cprint(self.requestline, 'green', force_color=True)

        # Print the search
        search = self.requestline.split(' ')[1][1:].split('?')[0]
        cprint('Search: ' + search, 'blue', force_color=True)

        try:
            if search == '':
                contents = Path(folder + 'main.html').read_text()
            elif search == 'listSpecies':
                lim = self.requestline.split('lim=')[1].split(' ')[0]
                cprint('Limit: ' + lim, 'blue', force_color=True)
                cprint('URL: ' + server + get_ep(search), 'blue', force_color=True)

                if lim == '' or lim.isdigit():
                    info = get_info(get_ep(search))  # get dict
                    tot_spc = len(info['species'])  # get number of total species in ensemble

                    if lim == '' or int(lim) > tot_spc:
                        lim = tot_spc  # if user does not input a limit, all species will be printed

                    if lim == '1':
                        spclist = 'is: <br><ul>'  # create string of species names in list format
                    else:
                        spclist = 'are: <br><ul>'

                    for n in range(int(lim)):
                        spclist += '<li>' + info['species'][n]['display_name'] + ' </li>'
                    spclist += '</ul>'
                    contents = (
                        Path(folder + 'species_list.html').read_text().replace('{lim}', str(lim)).replace('{tnum}',
                                                                                                          str(tot_spc)).replace(
                            '{content}', spclist))  # insert list of species into html
                else:
                    contents = Path(folder + 'error.html').read_text().replace('Resource not available',
                                                                               'Only numbers allowed')
            elif search == 'karyotype':
                species_input = self.requestline.split('spc0=')[1].split(' ')[0].lower()
                info = get_info(get_ep('1'))  # get dict all species
                name = ''  # get the name of the species to get the chromosomes
                for n in info['species']:
                    if n['display_name'].lower() == species_input:
                        name += n['name']
                species = get_info(get_ep(search, '/' + name))  # get dict of the species
                karyotype = species['karyotype']  # get list of the chromosome names
                chromosomes = 'The name of the chromosomes of a ' + name + 'are: <br><ul>'  # create message
                for n in karyotype:
                    chromosomes += '<li>' + n + '</li>'
                contents = Path(folder + 'karyotype.html').read_text().replace('{chromosomes}',
                                                                               chromosomes)  # insert message into html
            elif search == 'chromosomeLength':
                contents = 'a'
            else:
                contents = Path(folder + 'error.html').read_text()
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
