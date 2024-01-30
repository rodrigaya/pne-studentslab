# Write a program (without creating any function) that prints on the console the first 11 terms of the Fibonacci series (starting from 0).

f = 0
s = 1

for n in range (11):
    res = f + s
    print(f, end=' ')
    f = s
    s = res


