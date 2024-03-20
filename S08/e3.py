import socket
from Client0 import Client
from termcolor import cprint

# SERVER IP, PORT
PORT = 8080
IP = "127.0.0.1"  # depends on the computer the server is running

while True:
    msg = ('Hello!')
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((IP, PORT))
    s.send(str.encode(msg))
    cprint(s.recv(100000000).decode("utf-8"), 'blue')
    s.close()
    break
