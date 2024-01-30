# Convert the previous program into the function fibon(n) that calculates the nth Fibonacci term and return it
# The main program should call the fibon() function and print the 5th, 10th and 15th terms in the console

def fibon(n):
    f = 0
    s = 1

    for i in range(1, n + 1):
        res = f + s
        if i == n:
            result = 'The ' + str(n) + 'th fibonacci term is: ' + str(s)
        f = s
        s = res
    return result

print(fibon(5))
print(fibon(10))
print(fibon(15))