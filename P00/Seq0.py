from pathlib import Path


def seq_ping():
    print('OK')


def seq_read_fasta(filename):
    file_contents = Path(filename).read_text()
    seq_list = file_contents.split('\n')
    seq = ''
    for n in range(1, len(seq_list)):
        seq += seq_list[n].replace('\n', '')
    return seq


def seq_len(seq):
    return len(seq)


def seq_count_base(seq, base):
    n_b = 0
    for n in seq:
        if n == base:
            n_b += 1
    return n_b


def seq_count(seq):
    unique = []
    n_unique = []
    for n in seq:
        if n not in unique:
            unique.append(n)
    unique = sorted(unique)
    for n in unique:
        n_unique.append(seq_count_base(seq, n))
    return dict(zip(unique, n_unique))


def seq_reverse(seq):
    length = seq_len(seq)
    reverse = ''
    for n in range(length):
        reverse += seq[length - n - 1]
    return reverse


def seq_complement(seq):
    corr = {'A': 'U', 'T': 'A', 'C': 'G', 'G': 'C'}
    comp = ''
    for n in seq:
        comp += corr[n]
    return comp
