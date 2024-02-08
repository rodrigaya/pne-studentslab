from Seq0 import seq_reverse, seq_read_fasta

print(seq_read_fasta('../S04/Sequences/U5.fa'))
print(seq_reverse(seq_read_fasta('../S04/Sequences/U5.fa'))[0:20])