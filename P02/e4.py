from Client0 import Client
from Seq1 import Seq

PRACTICE = 2
EXERCISE = 3

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

folder = '../S04/Sequences/'
files = ['U5.fa', 'ADA.fa', 'FRAT1.fa', 'FXN.fa', 'RNU6_269P.fa']

IP = "212.128.255.81"
PORT = 8081

c = Client(IP, PORT)
print(c)

...
for n in files:
    s = Seq()
    s.seq_read_fasta(folder + n)
    print(f"Sending {n.split(',')[0]} gene to the sever...")
    response = c.talk("Testing!!!")
    print(f'To server: {(Seq(s).__str__())}')
    print(f"Response: {response}")
...
