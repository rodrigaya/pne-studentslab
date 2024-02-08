from Seq0 import seq_len, seq_read_fasta

folder = '../S04/Sequences/'
paths = ['U5.fa', 'ADA.fa', 'FRAT1.fa', 'FXN.fa']
lengths = []
for n in paths:
    lengths.append(seq_len(seq_read_fasta(folder + n)))

data = dict(zip(paths, lengths))

print('-----| Exercise 3 |------')
for n in data:
    print('Gene ' + n.split('/')[-1].split('.')[0] + ' -> Length: ' + str(data[n]))
