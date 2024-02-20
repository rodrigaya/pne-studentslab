from Seq1 import Seq

print('-----| Practice 1, Exercise 5 |------')
# -- Create a Null sequence
s1 = Seq()

# -- Create a valid sequence
s2 = Seq("ACTGA")

# -- Create an invalid sequence
s3 = Seq("Invalid sequence")
seqs = [s1, s2, s3]
for n in seqs:
    print(f'Sequence {seqs.index(n) + 1}: (Length: {n.len()}) {n} \n  A: ' + str(n.count_base('A')) + ',   C: ' + str(
        n.count_base('C')) + ',   T: ' + str(n.count_base('T')) + ',   G: ' + str(n.count_base('G')))
