import http.server
import socketserver
from termcolor import cprint
from pathlib import Path
import http.client
import json
import pprint
from Seq1 import Seq

server = "rest.ensembl.org"


def get_ep(search, name=None):
    params = '?content-type=application/json'
    if search == 'listSpecies':
        endpoint = '/info/species'
    elif search == 'geneSeq':
        endpoint = '/lookup/symbol/homo_sapiens/' + name
    elif search == 'getSequenceById':
        endpoint = '/sequence/id/' + name
    elif search == 'getInfoGeneById':
        endpoint = '/lookup/id/' + name
    elif search == 'geneList':
        endpoint = 'overlap/region/human/' + name
        params = '?feature=gene;feature=transcript;feature=cds;feature=exon;content-type=application/json'
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


def get_name(input_species):
    info = get_info(get_ep('listSpecies'))  # get dict all species
    name = ''  # get the scientific name that corresponds to the given name
    for n in info['species']:
        if n['display_name'].lower() == input_species.lower():
            name += n['name']
    return name


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
                if self.requestline.__contains__('limit='):
                    lim = self.requestline.split('limit=')[1].split(' ')[0]
                    cprint('Limit: ' + lim, 'blue', force_color=True)
                else:
                    lim = ''
                    cprint('Limit: none', 'blue', force_color=True)
                cprint('URL: ' + server + get_ep(search), 'blue', force_color=True)

                if (lim == '' or lim.isdigit()) and lim != '0':
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
                    contents = Path(folder + 'species_list.html').read_text().format(str(tot_spc), str(lim), spclist)
                    # insert list of species into html
                else:
                    contents = Path(folder + 'error.html').read_text().format('Incorrect limit entered')

            elif search == 'karyotype':
                input_species = self.requestline.split('species=')[1].split(' ')[0].lower().replace('+', ' ')
                cprint('Species: ' + input_species, 'blue', force_color=True)
                name = get_name(input_species)
                species = get_info(get_ep(search, '/' + name))  # get dict of the species
                pprint.pp(species)
                karyotype = species['karyotype']  # get list of the chromosome names
                chromosomes = 'The name of the chromosomes of a ' + input_species + ' ("' + name + '") are: <br><ul>'  # create message
                for n in karyotype:
                    chromosomes += '<li>' + n + '</li>'
                contents = Path(folder + 'karyotype.html').read_text().format(chromosomes)  # insert message into html
            elif search == 'chromosomeLength':
                input_species = self.requestline.split('species=')[1].split('&chromo=')[0].lower()  # get input name
                cprint('Species: ' + input_species, 'blue', force_color=True)
                name = get_name(input_species)  # get scientific name of species
                if name != '':
                    dict_species = get_info(get_ep(search, '/' + name))  # get dict of the species
                    chromosome = self.requestline.split('chromo=')[1].split(' ')[0].upper()  # get input chromosome
                    cprint('Chromosome: ' + chromosome, 'blue', force_color=True)
                    found = False
                    for n in dict_species['top_level_region']:  # search for matches of the chromosome in the species
                        if n['name'] == chromosome:
                            found = True  # stop execution of error page
                            contents = Path(folder + 'chromosomeLength.html').read_text().format(str(n['length']))
                        elif not found:
                            contents = Path(folder + 'error.html').read_text().format('Chromosome not found')
                else:
                    contents = Path(folder + 'error.html').read_text().format('Species not found')
            elif search == 'geneSeq':
                input_gene = self.requestline.split('gene=')[1].split(' ')[0].upper()  # get input gene
                cprint('Gene: ' + input_gene, 'blue', force_color=True)
                gene_id = get_info(get_ep(search, input_gene))['id']  # get corresponding id to gene name
                gene_seq = get_info(get_ep('getSequenceById', gene_id))['seq']  # get seq of gene by id
                contents = Path(folder + 'geneSeq.html').read_text().format(input_gene, gene_seq)
            elif search == 'geneInfo':
                input_gene = self.requestline.split('gene=')[1].split(' ')[0].upper()  # get input gene
                cprint('Gene: ' + input_gene, 'blue', force_color=True)
                gene_info = get_info(get_ep('geneSeq', input_gene))  # get dict of gene info
                contents = Path(folder + 'geneInfo.html').read_text().format(input_gene, gene_info['start'],
                                                                             gene_info['end'],
                                                                             gene_info['end'] - gene_info['start'],
                                                                             gene_info['id'],
                                                                             gene_info['seq_region_name'])
            elif search == 'geneCalc':
                input_gene = self.requestline.split('gene=')[1].split(' ')[0].upper()  # get input gene
                cprint('Gene: ' + input_gene, 'blue', force_color=True)
                gene_id = get_info(get_ep('geneSeq', input_gene))['id']  # get corresponding id to gene name
                seq = Seq(get_info(get_ep('getSequenceById', gene_id))['seq'])  # get seq of gene by id
                print(seq.len())
                pprint.pp(seq.count())
                contents = Path(folder + 'geneCalc.html').read_text().format(input_gene, seq.len(),
                                                                             seq.count_base('A'),
                                                                             ((seq.count_base(
                                                                                 'A') / seq.len()) * 100).__round__(1),
                                                                             seq.count_base('C'),
                                                                             ((seq.count_base(
                                                                                 'C') / seq.len()) * 100).__round__(1),
                                                                             seq.count_base('T'),
                                                                             ((seq.count_base(
                                                                                 'T') / seq.len()) * 100).__round__(1),
                                                                             seq.count_base('G'),
                                                                             ((seq.count_base(
                                                                                 'G') / seq.len()) * 100).__round__(1))
            elif search == 'geneList':
                input_chromo = self.requestline.split('chromo=')[1].split('&start=')[0].upper()  # get input chromosome
                cprint('Chromosome: ' + input_chromo, 'blue', force_color=True)
                data = get_info(get_ep('/karyotype', '/homo_sapiens'))[
                    'top_level_region']  # get data of the human chromosomes
                chromo_list = []
                chromo_len_list = []
                for n in data:  # create dictionary of chromosome with its associated length
                    if n['coord_system'] == 'chromosome':
                        chromo_list.append(n['name'])
                        chromo_len_list.append(n['length'])
                chromo_len_dict = dict(zip(chromo_list, chromo_len_list))
                start = self.requestline.split('start=')[1].split('&end=')[0].upper()  # get input start
                if start == '':  # correction measure
                    start = '0'
                cprint('Start: ' + start, 'blue', force_color=True)
                end = self.requestline.split('end=')[1].split(' ')[0].upper()  # get input end
                if end == '':  # correction measure
                    end = chromo_len_dict[input_chromo]
                cprint('End: ' + end, 'blue', force_color=True)
                if input_chromo in chromo_len_dict.keys():  # check that the chromosome is valid
                    if start.isdigit() and end.isdigit():  # check that the range format is valid
                        if int(start) < int(end):  # check that there is a valid range 
                            name = input_chromo + ':' + start + '-' + end  # addition to endpoint
                            dict_seq = get_info(get_ep(search, name))
                            html_list_genes = ''
                            for n in dict_seq:  # create list of valid gene names
                                # (not considering those which don't have external name)
                                if 'external_name' in n.keys():
                                    html_list_genes += '<li>' + n['external_name'] + '</li>'
                            if html_list_genes != '':
                                genes = html_list_genes
                            else:
                                genes = 'No genes could be found in the range given'
                            contents = Path(folder + 'geneList.html').read_text().format(input_chromo, start, end,
                                                                                         genes)
                        else:
                            contents = Path(folder + 'error.html').read_text().format('Range is not valid')
                    else:
                        contents = Path(folder + 'error.html').read_text().format('Range format is not valid')
                else:
                    contents = Path(folder + 'error.html').read_text().format('Chromosome not found')
            else:
                contents = Path(folder + 'error.html').read_text().format('Input is not valid')

        except FileNotFoundError:
            contents = Path('html/error.html').read_text().format('File not found')

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
