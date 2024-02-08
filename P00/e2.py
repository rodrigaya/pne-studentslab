from Seq0 import seq_read_fasta

path = '../S04/Sequences/U5.fa'
print('DNA file:', path.split('/')[-1])

file = seq_read_fasta(path)
print('The first 20 bases are:' + '\n' + file[:19])
