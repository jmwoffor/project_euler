# Project Euler 34
# Find the sum of all numbers which are equal to the sum of the factorial of their digits
# 1 and 2 are not included

def factorial(n):
    i = 1
    x = 1
    while i <= n:
        x *= i
        i += 1
    return x

i = 3
total = 0

while i < 1000000:
    digits = [int(x) for x in str(i)]
    fsum = 0
    for j in digits:
        fsum += factorial(int(j))
    if fsum == i:
        print(fsum)
        total += i
    i += 1

print(total)
