seq = input('Introduce the sequence: ').upper()
print('Total length: ' + str(len(seq)))

dict = {'A': 0, 'C': 0, 'T': 0, 'G': 0}
for n in seq:
    dict[n] += 1

for n in dict.keys():
    print(n + ': ' + str(dict[n]))