from pathlib import Path


class Seq:

    def __init__(self, strbases=None):
        if type(strbases) == str and strbases.count('A') + strbases.count('C') + strbases.count('G') + strbases.count(
                'T') == len(strbases):
            print("New sequence created!")
            self.strbases = strbases
        elif strbases == None:
            print("Null sequence created")
            self.strbases = ('NULL')
        else:
            print('INVALID sequence!')
            self.strbases = 'ERROR'

    def __str__(self):
        return self.strbases

    def len(self):
        if self.strbases == 'ERROR' or self.strbases == 'NULL':
            return 0
        else:
            return len(self.strbases)

    def count_base(self, base):
        if self.strbases == 'ERROR' or self.strbases == 'NULL':
            return 0
        else:
            return self.strbases.count(base)

    def count(self):
        basis = ['A', 'C', 'T', 'G']
        numbers = []
        if self.strbases == 'ERROR' or self.strbases == 'NULL':
            return dict(zip(basis, [0, 0, 0, 0]))
        else:
            for n in basis:
                numbers.append(self.strbases.count(n))
            return dict(zip(basis, numbers))

    def seq_reverse(self):
        length = len(self.strbases)
        reverse = ''
        if self.strbases == 'ERROR' or self.strbases == 'NULL':
            return 'ERROR'
        else:
            for n in range(length):
                reverse += self.strbases[length - n - 1]
            return reverse

    def seq_complement(self):
        corr = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
        comp = ''
        if self.strbases == 'ERROR' or self.strbases == 'NULL':
            return 'ERROR'
        else:
            for n in self.strbases:
                comp += corr[n]
            return comp

    def seq_read_fasta(self, filename):
        file_contents = Path(filename).read_text()
        seq_list = file_contents.split('\n')
        seq = ''
        for n in range(1, len(seq_list)):
            seq += seq_list[n].replace('\n', '')
        self.strbases = seq
