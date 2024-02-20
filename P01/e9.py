from Seq1 import Seq

print('-----| Practice 1, Exercise 9 |------')
# -- Create a Null sequence
s = Seq()

seqs = [s.seq_read_fasta('../S04/Sequences/U5.fa')]
for n in seqs:
    print(
        f'Sequence {seqs.index(n) + 1}: (Length: {n.len()}) {n} \n  Bases: {n.count()} \n  Rev:  {n.seq_reverse()} \n  '
        f'Comp: {n.seq_complement()}')
