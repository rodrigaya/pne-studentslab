import socket
from Client0 import Client
from termcolor import cprint

# SERVER IP, PORT
PORT = 8080
IP = "212.128.255.81"  # depends on the computer the server is running

while True:
    msg = ('Get 1')
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((IP, PORT))
    s.send(str.encode(msg))
    cprint(s.recv(100000000).decode("utf-8"), 'blue')
    s.close()
    break
