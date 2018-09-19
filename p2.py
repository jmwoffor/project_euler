# Project Euler #2: Find the sum of even numbered terms in the Fibonacci sequence
# up to 4 million

fib0 = 0
fib1 = 1
sum = 0

bool = True
while bool:
    new = fib0 + fib1
    fib0 = fib1
    fib1 = new
    if fib1 % 2 == 0:
        sum += fib1
    elif fib1 >= 4*10**6:
        print(sum)
        break
