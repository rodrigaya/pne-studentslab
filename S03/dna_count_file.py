def read_file(filename):
    seq = ''
    with open(filename, 'r') as f:
        for n in f.read():
            if n != '\n':
                seq += n
    return seq

def count_bases(seq):
    print('Total length: ' + str(len(seq)))

    dict = {'A': 0, 'C': 0, 'T': 0, 'G': 0}
    for n in seq:
        dict[n] += 1

    for n in dict.keys():
        print(n + ': ' + str(dict[n]))

count_bases(read_file('dna.txt'))