import http.client
import json
from termcolor import cprint
from Seq1 import Seq

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

for gene in genes:
    idg = genes[gene]

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
    print(gene)
    cprint('Description: ', 'yellow', end='', force_color=True)
    print(response['desc'])

    g = Seq(response['seq'])
    cprint('Total length: ', 'yellow', end='', force_color=True)
    print(g.len())
    count = g.count()
    for base in count:
        cprint(base, 'blue', end='', force_color=True)
        print(':', str(count[base]) + ' (' + str(((count[base] / g.len()) * 100).__round__(1)) + '%)')

    biggest = 0
    b = ''
    for base in count:
        if count[base] > biggest:
            biggest = count[base]
            b = base
    cprint('Most frequent base: ', 'yellow', end='', force_color=True)
    print(b)
