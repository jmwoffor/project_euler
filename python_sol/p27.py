# Project Euler 27
# Consider quadratics of the form: n^2 + an + b where |a| < 1000 and |b| <= 1000
# Find the product of the coefficients, a and b, for the quadratic expression that
# produces the maximum number of primes for consecutive values of n, starting with n = 0

# b must be prime since we start with n = 0

def is_prime(n):
    if n<= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i*i <= n:
        if n % i == 0 or n % (i+2) == 0:
            return False
        i += 6
    return True

b = [] # b has to be prime
for i in range(1000):
    if is_prime(i) == True:
        b.append(i)

n = 0
primes_count = 0
max_a = 0
max_b = 0
max_count = 0

for i in range(-1000,1000):
    for j in b:
        bool = True
        while bool == True:
            if is_prime(n**2 + i*n + j) == True:
                n += 1
            else:
                if n > max_count:
                    max_count = n
                    max_a = i
                    max_b = j
                    n = 0
                    bool = False
                else:
                    n = 0
                    bool = False

print(max_a)
print(max_b)
print(max_count)
print(max_a*max_b)
