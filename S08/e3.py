import socket

# SERVER IP, PORT
PORT = 8081
IP = "212.128.255.76"  # depends on the computer the server is running

while True:
    msg = 'holiwis'
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((IP, PORT))
    s.send(str.encode(msg))
    s.close()
    break
