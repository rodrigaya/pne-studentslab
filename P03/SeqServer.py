import socket

PORT = 8080
IP = "127.0.0.1"
MAX_OPEN_REQUESTS = 5

number_con = 0

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    serversocket.bind((IP, PORT))
    serversocket.listen(MAX_OPEN_REQUESTS)

    while True:
        print("Waiting for connections at {}, {} ".format(IP, PORT))
        (clientsocket, address) = serversocket.accept()

        number_con += 1

        print("CONNECTION: {}. From the IP: {}".format(number_con, address))

        msg = clientsocket.recv(2048).decode("utf-8")
        if msg == 'PING':
            print('OK')

        message = "OK!\n"
        send_bytes = str.encode(message)
        clientsocket.send(send_bytes)
        clientsocket.close()

except socket.error:
    print("Problems using ip {} port {}. Is the IP correct? Do you have port permission?".format(IP, PORT))

except KeyboardInterrupt:
    print("Server stopped by the user")
    serversocket.close()


def ping():
    print('OK')


def get(n):
    seqs = [1, 2, 3, 4]
    seq = seqs[n]
    return seq

def info(seq)
def wtd(msg):
    if msg == 'PING':
        ping()

    if msg.contains('GET'):
        get(int(msg[-1]))

    if msg == 'INFO':
        info(seq)

