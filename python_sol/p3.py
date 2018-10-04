# Project Euler #3
# Find the greatest prime factor of 600851475143

N = 600851475143
factors = []
d = 2
while N > 1:
    while N % d == 0:
        factors.append(d)
        N /= d
    d += 1

print(max(factors))
