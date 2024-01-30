# Write a function called fibosum(n) that calculates
# the addition of the n first fibonacci terms. The main program should call this function twice, with the arguments n=5 and n=10.

def fibosum(n):
    sum = 0

    f = 0
    s = 1

    for i in range(1, n + 1):
        res = f + s
        f = s
        s = res
        sum += f
    result = 'The sum of the first ' + str(n) + ' terms of the Fibonacci series: ' + str(sum)
    return result


print(fibosum(5))
print(fibosum(10))