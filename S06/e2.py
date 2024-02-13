from seq01 import Seq

class Seq:
    def __init__(self, strbases):
        if type(strbases) == str and strbases.count('A') + strbases.count('C') + strbases.count('G') + strbases.count(
                'T') == len(strbases):
            self.strbases = strbases
            print("New sequence created!")
        else:
            print('INCORRECT Sequence detected')
            self.strbases = 'ERROR'

        return

    def __str__(self):
        """Method called when the object is being printed"""
        # -- We just return the string with the sequence
        return self.strbases

# herencia

s1 = Seq("ACCTGC")
s2 = Seq("Hello? Am I a valid sequence?")
print(f"Sequence 1: {s1}")
print(f"Sequence 2: {s2}")