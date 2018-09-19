# Project Euler #7
# Find the 10001st prime number

# Gonna try to use the Sieve of Eratosthenes to find primes
n = 200000 # total numbers checked
pn = 10001 # will return pn^th prime
pc = 1 # prime counter, start at pc = 1 with 2
p = 2 # starter prime number
a = list(range(p,n,2))
notprime = [0,1]
def soe(pn,n):
    p = 2 # starter prime number
    pc = 1 # prime counter
    a = list(range(p,n,2))
    notprime = [0,1]
    while pc < pn:
        notprime.extend(list(range(0,n,p)))
        if p == 2:
            a = list(range(p,n))
        else:
            a = list(range(p,n,2))
        for i in a:
            if i not in notprime:
                p = i
                pc += 1
                return p
                break

print(soe(pn,n))
