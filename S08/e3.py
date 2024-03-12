import socket
from Client0 import Client

# SERVER IP, PORT
PORT = 8080
IP = "127.0.0.1"  # depends on the computer the server is running

while True:
    msg = 'GET 4'
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((IP, PORT))
    s.send(str.encode(msg))
    print(s.recv(100000000).decode("utf-8"))
    s.close()
    break
