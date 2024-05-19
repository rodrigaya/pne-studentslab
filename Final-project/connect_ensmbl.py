import json
import http.client
import pprint

server = "rest.ensembl.org"


def get_ep(search, name=None, gene=None):
    params = '?content-type=application/json'
    if search == 'listSpecies':
        endpoint = '/info/species'
    elif search == 'geneSeq':
        endpoint = '/lookup/symbol/homo_sapiens/'
    else:
        endpoint = '/info/assembly' + name

    return endpoint + gene + params


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


pprint.pp(get_info(get_ep('geneSeq', None, 'FRAT1')))
