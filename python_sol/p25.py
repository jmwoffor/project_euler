# Project Euler 25
# What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

import math

ind = 2 # starting index
def digits(n): # this is apparently faster than converting to a str and taking the len()
    return int(math.log10(n))+1

fib0 = 1
fib1 = 1

while digits(fib1) < 1000:
    new = fib0 + fib1
    fib0 = fib1
    fib1 = new
    ind += 1

print(ind)
