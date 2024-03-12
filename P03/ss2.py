a = 'GET 4'


def get(n):
    seqs = [1, 2, 3, 4]
    seq = seqs[n - 1]
    return seq


n = a.strip().split(' ')[1]
print(n)
if type(n) == int:
    response = get(int(n))
    print(response)
