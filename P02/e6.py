from Client0 import Client
from Seq1 import Seq

PRACTICE = 2
EXERCISE = 5

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

file = '../S04/Sequences/FRAT1.fa'

IP = "212.128.255.31"
PORT1 = 8080
PORT2 = 8081

c = Client(IP, PORT1)
d = Client(IP, PORT2)
print(c)
print(d)
s = Seq()
s.seq_read_fasta(file)
print('Gene ' + file.split('/')[-1].replace('.fa', '') + ': ' + str(s))
seq = str(s)
a = 0

c.talk('Sending ' + str(file.split('/')[-1].replace('.fa', '')) + ' gene to the sever, in fragments of 10 bases...')
d.talk('Sending ' + str(file.split('/')[-1].replace('.fa', '')) + ' gene to the sever, in fragments of 10 bases...')

for n in range(10):
    newseq = ''
    for m in range(10):
        newseq += seq[m + a]
    a += 10
    print('Fragment ' + str(n + 1) + ': ' + newseq)
    if n % 2 == 0:
        c.talk('Fragment ' + str(n + 1) + ': ' + newseq)
    if n % 2 == 1:
        d.talk('Fragment ' + str(n + 1) + ': ' + newseq)
