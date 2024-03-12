import socket


def get(n):
    seqs = ['A', 'C', 'T', 'G']
    seq = seqs[n - 1]
    return seq


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
        if msg == "PING":
            print("PING command!")
            response = "OK!\n"

            clientsocket.send(response.encode())
            print(response)

        if msg.__contains__('GET'):
            print("GET command!")
            n = msg.strip().split(' ')[1]
            if n.strip().isdigit():
                response = str(get(int(n.strip())))
            else:
                response = 'Unexpected value'
            clientsocket.send(response.encode())
            print(response)

        # message = "OK!\n"
        # send_bytes = str.encode(message)
        # clientsocket.send(send_bytes)
        clientsocket.close()

except socket.error:
    print("Problems using ip {} port {}. Is the IP correct? Do you have port permission?".format(IP, PORT))

except KeyboardInterrupt:
    print("Server stopped by the user")
    serversocket.close()

# def info(seq)
