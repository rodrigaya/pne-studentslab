from Seq0 import seq_reverse, seq_read_fasta

path = '../S04/Sequences/U5.fa'
print('------| Exercise 6 |------' +
      '\nGene ' + path.split('/')[-1].replace('.fa', '') + ':' +
      '\nFragement: ' + seq_read_fasta(path)[0:20] +
      '\nReverse: ' + seq_reverse(seq_read_fasta('../S04/Sequences/U5.fa'))[-20:])
