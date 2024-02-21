from Seq1 import Seq

print('-----| Practice 1, Exercise 10 |------')

files = ['../S04/Sequences/U5.fa', '../S04/Sequences/ADA.fa', '../S04/Sequences/FRAT1.fa', '../S04/Sequences/FXN.fa',
         '../S04/Sequences/RNU6_269P.fa']

for n in files:
    s = Seq()
    s.seq_read_fasta(n)
    d = s.count()
    maxi = sorted(d.values())[-1]
    unique = []
    for m in d.values():
        if m not in unique:
            unique.append(m)
    key = []
    for m in d.keys():
        if len(unique) < len(d.values()):
            num = len(d.values()) - len(unique)
            if d[m] == maxi:
                key.append(m)
        else:
            if d[m] == maxi:
                key.append(m)
    print('Gene ' + str(n.split('/')[-1].replace('.fa', '')) + ':' + ' Most frequent Base: ' +
          str(key).replace("'", '')[1:-1])
