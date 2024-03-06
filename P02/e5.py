from Client0 import Client
from Seq1 import Seq

PRACTICE = 2
EXERCISE = 5

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

file = '../S04/Sequences/FRAT1.fa'

IP = "212.128.255.81"
PORT = 8081

c = Client(IP, PORT)
print(c)
s = Seq()
s.seq_read_fasta(file)
print('\nGene ' + file.split('/')[-1].replace('.fa', '') + ': ' + str(s) + '\n')
seq = str(s)
d = 0

print('To server: Sending ' + str(
    file.split('/')[-1].replace('.fa', '')) + ' gene to the sever, in fragments of 10 bases...')
print('From server: ' + str(c.talk('Sending ' + str(
    file.split('/')[-1].replace('.fa', '')) + ' gene to the sever, in fragments of 10 bases...')))

for n in range(5):
    newseq = ''
    for m in range(10):
        newseq += seq[m + d]
    d += 10
    print('To server: Fragment ' + str(n + 1) + ': ' + newseq)
    print(f"From server: {c.talk('Fragment ' + str(n + 1) + ': ' + newseq)}")



