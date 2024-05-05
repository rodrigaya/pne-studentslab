def rev(msg):
    result = ''
    ll = len(msg)
    for n in range(ll):
        result += msg[ll - n - 1]
    return result

print(rev('ACTG'))
