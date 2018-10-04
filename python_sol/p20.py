# Project Euler 20
# Find the sum of the digits in the number 100!

def factorial(n):
    i = 1
    x = 1
    while i <= n:
        x *= i
        i += 1
    return x

x = str(factorial(100))

sum = 0
for i in x:
    sum += int(i)

print(sum)
