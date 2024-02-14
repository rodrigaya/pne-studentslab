class Seq:
    """A class for representing sequences"""

    def __init__(self, strbases=None):
        if type(strbases) == str and strbases.count('A') + strbases.count('C') + strbases.count('G') + strbases.count(
                'T') == len(strbases):
            self.strbases = strbases
            print("New sequence created!")
        else:
            print('INCORRECT Sequence detected')
            self.strbases = 'ERROR'

    def __str__(self):
        """Method called when the object is being printed"""
        # -- We just return the string with the sequence
        return self.strbases

    def len(self):
        """Calculate the length of the sequence"""
        return len(self.strbases)

def print_seqs(seq_list):
    seq_n = len(seq_list)
    for n in seq_list:
        print('Sequence ' + str(seq_list.index(n)) + ': ' + '(Length: ' + str(len(str(n))) + ') ' + str(n))

def generate_seqs(pattern, number):
    list_of_patterns = []
    for n in range(number):
        list_of_patterns.append(Seq(pattern + pattern * n))
    return list_of_patterns


seq_list1 = generate_seqs("A", 3)
seq_list2 = generate_seqs("AC", 5)

print("List 1:")
print_seqs(seq_list1)

print("List 2:")
print_seqs(seq_list2)
