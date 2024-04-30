import http.server
import socketserver
# import termcolor
from pathlib import Path


def info(msg):
    length = len(msg)
    new = []
    times = []
    for n in msg:
        if n not in new:
            new.append(n)
    for n in new:
        time = 0
        for ñ in msg:
            if n == ñ:
                time += 1
        times.append(time)
    corr = dict(zip(new, times))
    result = \
        'Total length: ' + str(length) + '\n'
    for n in new:
        string = ''
        for a in range(len(new)):
            string += new[a] + ': ' + corr[new[a]] + ' (' + str((int(corr[new[a]])/length) * 100) + '%)'
    result += string



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
        # termcolor.cprint(self.requestline, 'green')
        print(self.requestline, 'green')

        # IN this simple server version:
        # We are NOT processing the client's request
        # It is a happy server: It always returns a message saying
        # that everything is ok
        folder = 'html/'
        search = self.requestline.split(' ')[1][1:].split('?')[0]
        print(search)
        try:
            if search == '':
                contents = Path(folder + 'index2.html').read_text()
            elif search == 'ping':
                contents = Path(folder + search + '.html').read_text()
            elif search == 'get':
                n = int(self.requestline.split(' ')[1][1:].split('=')[1])
                seqs = ['ACCTCCTCTCCAGCAATGCCAACCCCAGTCCAGGCCCCCATCCGCCCAGGATCTCGATCA',
                        'AAAAACATTAATCTGTGGCCTTTCTTTGCCATTTCCAACTCTGCCACCTCCATCGAACGA',
                        'CAAGGTCCCCTTCTTCCTTTCCATTCCCGTCAGCTTCATTTCCCTAATCTCCGTACAAAT',
                        'CCCTAGCCTGACTCCCTTTCCTTTCCATCCTCACCAGACGCCCGCATGCCGGACCTCAAA',
                        'AGCGCAAACGCTAAAAACCGGTTGAGTTGACGCACGGAGAGAAGGGGTGTGTGGGTGGGT']
                # contents = create_html('get', 'Sequence number ' + str(n), seqs[n])
                contents = Path(folder + search + '.html').read_text().replace('{n}', str(n)).replace('{body}', seqs[n])
            elif search == 'gene':
                folder2 = '../S04/Sequences/'
                seq = self.requestline.split(' ')[1].split('=')[1]
                base = Path(folder2 + seq).read_text()
                body = base[base.find('\n'):].replace('\n', '')
                contents = Path(folder + search + '.html').read_text().replace('{gene}', seq).replace('{body}', body)
            elif search == 'operation':
                operation = self.requestline.split('&op=')[1].split('HTTP/')[0].strip()
                msg = self.requestline.split('&op=')[0].split('?msg=')[1].upper()
                print(operation)
                print(msg)
                if operation == 'info':
                    contents = Path(folder + search + '.html').read_text().replace('{seq}', msg).replace('{op}',
                                                                                                         operation).replace(
                        '{result}', str(info(msg)))
                elif operation == 'comp':
                    contents = 'a'
                elif operation == 'rev':
                    contents = 'a'
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
