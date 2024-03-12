import socket
from Seq1 import Seq
from termcolor import cprint


def get(n):
    seqs = ['A', 'C', 'T', 'G']
    seq = seqs[n - 1]
    return seq


def info(seq):
    s = Seq(seq)
    result = 'Sequence: ' + str(s) + '\nTotal length: ' + str(s.len()) + '\n' + 'A: ' + str(
        s.count_base('A')) + ' (' + str((s.count_base('A') / s.len()) * 100)[:4] + '%)' + '\nC: ' + str(
        s.count_base('C')) + ' (' + str((s.count_base('C') / s.len()) * 100)[:4] + '%)' + '\nT: ' + str(
        s.count_base('T')) + ' (' + str((s.count_base('T') / s.len()) * 100)[:4] + '%)' + '\nG: ' + str(
        s.count_base('G')) + ' (' + str((s.count_base('G') / s.len()) * 100)[:4] + '%)'
    return result


def comp(seq):
    return Seq(seq).seq_complement()


def rev(seq):
    return Seq(seq).seq_reverse()


def gene(gene):
    genes = ['U5', 'ADA', 'FRAT1', 'FXN', 'RNU6_269P']
    folder = '../S04/Sequences/'
    if gene in genes:
        s = Seq()
        s.seq_read_fasta(folder + gene + '.fa')
        result = s
    else:
        result = 'Invalid name'
    return result


def get_funct(funct, l, obj):
    cprint(funct, 'green')
    seq = msg[l:].strip()
    if len(seq) == 0:
        response = 'Enter a ' + obj + ' name'
    else:
        response = str(gene(seq))
    clientsocket.send(response.encode())
    cprint(response, 'blue')


PORT = 8080
IP = "212.128.255.81"
MAX_OPEN_REQUESTS = 5

number_con = 0

ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
try:
    ls.bind((IP, PORT))
    ls.listen(MAX_OPEN_REQUESTS)

    while True:
        print("Waiting for connections at {}, {} ".format(IP, PORT))
        (clientsocket, address) = ls.accept()

        number_con += 1

        print("CONNECTION: {}. From the IP: {}".format(number_con, address))

        msg = clientsocket.recv(2048).decode("utf-8").strip().upper()
        if msg == "PING":
            print("PING command!")
            response = "OK!\n"

            clientsocket.send(response.encode())
            print(response)

        if msg.startswith('GET'):
            print("GET command!")
            n = msg.split(' ')[1].strip()
            if n.isdigit() and 0 < int(n) < 5:
                response = str(get(int(n)))
            else:
                response = 'Unexpected value'
            clientsocket.send(response.encode())
            print(response)

        if msg.startswith('INFO'):
            get_funct('info', 4, 'sequence')

        if msg.startswith('COMP'):
            get_funct('comp', 4, 'sequence')

        if msg.startswith('REV'):
            get_funct('rev', 3, 'sequence')

        if msg.startswith('GENE'):
            get_funct('gene', 4, 'gene')

        clientsocket.close()

except socket.error:
    print("Problems using ip {} port {}. Is the IP correct? Do you have port permission?".format(IP, PORT))

except KeyboardInterrupt:
    print("Server stopped by the user")
    ls.close()

# def info(seq)
