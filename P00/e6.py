from Seq0 import seq_reverse, seq_read_fasta


print('------| Exercise 6 |------' +
      '\nFragement: ' + seq_read_fasta('../S04/Sequences/U5.fa')[0:20] +
      '\nReverse: ' + seq_reverse(seq_read_fasta('../S04/Sequences/U5.fa'))[-20:])
