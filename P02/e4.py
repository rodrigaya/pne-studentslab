from Client0 import Client
from Seq1 import Seq

PRACTICE = 2
EXERCISE = 4

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

folder = '../S04/Sequences/'
files = ['U5.fa', 'ADA.fa', 'FRAT1.fa']

IP = "212.128.255.81"
PORT = 8081

c = Client(IP, PORT)
print(c)

...
for n in files:
    s = Seq()
    s.seq_read_fasta(folder + n)
    response = c.talk("Testing!!!")
    print(f'To server: Sending {n.split(".")[0]} gene to the sever...')
    print(f"From server: {c.talk('Sending ' + str(n.split('.')[0]) + ' gene to the sever...')}")
    print(f'To server: {s}')
    print(f"From server: {c.talk(str(s))}\n")
    ...
