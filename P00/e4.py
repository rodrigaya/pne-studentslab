from Seq0 import seq_count_base, seq_read_fasta

paths = ['../S04/Sequences/U5.fa', '../S04/Sequences/ADA.fa', '../S04/Sequences/FRAT1.fa',
         '../S04/Sequences/FXN.fa']
bases = ['A', 'C', 'T', 'G']
lengths = []
for n in paths:
    n_bs = []
    for m in bases:
        n_b = seq_count_base(seq_read_fasta(n), m)
        n_bs.append(n_b)
    lengths.append(dict(zip(bases, n_bs)))

data = dict(zip(paths, lengths))
print(data)

print('-----| Exercise 4 |------')
for n in data:
    print('\nGene ' + n.split('/')[-1].replace('.fa', '') + ':')
    for m in data[n].keys():
        print('  ' + m + ':' + str(data[n][m]))
a