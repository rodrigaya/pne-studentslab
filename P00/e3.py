from Seq0 import seq_len, seq_read_fasta


paths = ['../S04/Sequences/U5.fa', '../S04/Sequences/ADA.fa', '../S04/Sequences/FRAT1.fa',
         '../S04/Sequences/FXN.fa']
lengths = []
for n in paths:
    lengths.append(seq_len(seq_read_fasta(n)))

data = dict(zip(paths, lengths))

print('-----| Exercise 3 |------')
for n in data:
    print('Gene ' + n.split('/')[-1].split('.')[0] + ' -> Length: ' + str(data[n]))
