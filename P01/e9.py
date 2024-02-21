from Seq1 import Seq

print('-----| Practice 1, Exercise 9 |------')
# -- Create a Null sequence

seqs = ['../S04/Sequences/U5.fa']
for n in seqs:
    s = Seq()
    s.seq_read_fasta(n)
    print(
        f'Sequence {seqs.index(n) + 1}: (Length: {s.len()}) {n} \n  Bases: {s.count()} \n  Rev:  {s.seq_reverse()} \n  '
        f'Comp: {s.seq_complement()}')
