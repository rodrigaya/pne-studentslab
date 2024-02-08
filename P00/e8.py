from Seq0 import seq_read_fasta, seq_count

folder = '../S04/Sequences/'
paths = ['U5.fa', 'ADA.fa', 'FRAT1.fa', 'FXN.fa']
bases = ['A', 'C', 'T', 'G']
lengths = []

for n in paths:
    lengths.append(seq_count(seq_read_fasta((folder + n))))

data = dict(zip(paths, lengths))

print('-----| Exercise 8 |------')
for n in data:
    bigger = ''
    num = 0
    for m in data[n].keys():
        if data[n][m] > num:
            bigger = m
            num = data[n][m]
    print('Gene ' + n + ': ' + 'Most frequent base: ' + bigger)
