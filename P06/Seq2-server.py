import http.server
import socketserver
import termcolor
from pathlib import Path


def info(msg):
    result = 'Total length: '
    result += str(len(msg)) + '<p></p>'
    newchar = []
    for n in msg:
        if n not in newchar:
            newchar.append(n)
    for n in newchar:
        t = msg.count(n)
        result += n + ': ' + str(t) + ' (' + str(((t / len(msg)) * 100).__round__(1)) + '%)<p></p>'
    return result


def comp(msg):
    dcomp = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    result = ''
    for n in msg:
        result += dcomp[n]
    return result


def rev(msg):
    result = ''
    ll = len(msg)
    for n in range(ll):
        result += msg[ll - n - 1]
    return result


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
            elif search == 'ping':
                contents = Path(folder + search + '.html').read_text()
            elif search == 'get':
                n = int(self.requestline.split(' ')[1][1:].split('=')[1])
                seqs = ['ACCTCCTCTCCAGCAATGCCAACCCCAGTCCAGGCCCCCATCCGCCCAGGATCTCGATCA',
                        'AAAAACATTAATCTGTGGCCTTTCTTTGCCATTTCCAACTCTGCCACCTCCATCGAACGA',
                        'CAAGGTCCCCTTCTTCCTTTCCATTCCCGTCAGCTTCATTTCCCTAATCTCCGTACAAAT',
                        'CCCTAGCCTGACTCCCTTTCCTTTCCATCCTCACCAGACGCCCGCATGCCGGACCTCAAA',
                        'AGCGCAAACGCTAAAAACCGGTTGAGTTGACGCACGGAGAGAAGGGGTGTGTGGGTGGGT']
                contents = Path(folder + search + '.html').read_text().replace('{n}', str(n)).replace('{body}', seqs[n])
            elif search == 'gene':
                folder2 = '../S04/Sequences/'
                seq = self.requestline.split(' ')[1].split('=')[1]
                base = Path(folder2 + seq).read_text()
                body = base[base.find('\n'):].replace('\n', '')
                contents = Path(folder + search + '.html').read_text().replace('{gene}',
                                                                               seq.replace('.fa', '')).replace('{body}',
                                                                                                               body)
            elif search == 'operation':
                operation = self.requestline.split('&op=')[1].split('HTTP/')[0].strip()
                msg = self.requestline.split('&op=')[0].split('?msg=')[1].upper().strip()
                if msg.count('A') + msg.count('C') + msg.count('T') + msg.count('G') != len(msg):
                    contents = Path('html/error.html').read_text().replace('Resource not available',
                                                                           'Incorrect aminoacid bases')
                else:
                    print('Op: ' + operation)
                    print('Msg: ' + msg)
                    if operation == 'info':
                        contents = Path(folder + search + '.html').read_text().replace('{seq}', msg).replace('{op}',
                                                                                                             operation).replace(
                            '{result}', str(comp(msg)))
                    elif operation == 'comp':
                        contents = Path(folder + search + '.html').read_text().replace('{seq}', msg).replace('{op}',
                                                                                                             operation).replace(
                            '{result}', str(comp(msg)))
                    elif operation == 'rev':
                        contents = Path(folder + search + '.html').read_text().replace('{seq}', msg).replace('{op}',
                                                                                                             operation).replace(
                            '{result}', str(rev(msg)))
                    else:
                        contents = Path('html/error.html').read_text()
            else:
                contents = Path(folder + 'error.html').read_text()
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
