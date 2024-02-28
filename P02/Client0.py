import socket


class Client:

    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    def __str__(self):
        return f'Connection to SERVER at {self.ip}, PORT: {self.port}'

    def ping(self):
        print('OK')

    def talk(self, msg=None):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.ip, self.port))
        s.send(str.encode(msg))
        s.close()
