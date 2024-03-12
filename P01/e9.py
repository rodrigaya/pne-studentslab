from Seq1 import Seq

print('-----| Practice 1, Exercise 9 |------')

n = '../S04/Sequences/'
name = 'FRAT1.fa'
s = Seq()
s.seq_read_fasta(n + name)
print(s)

print(
    f'Sequence 1: (Length: {s.len()}) {n} \n  Bases: {s.count()} \n  Rev:  {s.seq_reverse()} \n  '
    f'Comp: {s.seq_complement()}')
