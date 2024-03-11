def ping():
    return 'OK'


def get(n):
    seqs = []
    seq = seqs[n]
    return seq


def info(seq):
    print('Seq: ' + str(seq))
    print('Total length: ' + str(len(seq)))
    if len(seq) != 0:
        print('A: ' + str(seq.count('A')) + '(' + str((seq.count('A') / len(seq)) * 100) + '%)')
        print('C: ' + str(seq.count('C')) + '(' + str((seq.count('C') / len(seq)) * 100) + '%)')
        print('T: ' + str(seq.count('T')) + '(' + str((seq.count('T') / len(seq)) * 100) + '%)')
        print('G: ' + str(seq.count('G')) + '(' + str((seq.count('G') / len(seq)) * 100) + '%)')

def comp(seq):

