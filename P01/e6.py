from Seq1 import Seq

print('-----| Practice 1, Exercise 6 |------')

s1 = Seq()
s2 = Seq("ACTGA")
s3 = Seq("Invalid sequence")

seqs = [s1, s2, s3]

for n in seqs:
    print(f'Sequence {seqs.index(n) + 1}: (Length: {n.len()}) {n} \n  Bases: {n.count()}')
