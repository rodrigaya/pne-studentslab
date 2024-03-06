import termcolor
from Client0 import Client

# SERVER IP, PORT
PORT = 8081
IP = "212.128.255.81"  # depends on the computer the server is running

for n in range(5):
    # -- Create a client object
    c = Client(IP, PORT)
    # print(c)

    ...
    # -- Send a message to the server
    print(f'To server: Message {n}')
    response = c.talk(f"Message {n}")
    print(f"From server: {response}")
