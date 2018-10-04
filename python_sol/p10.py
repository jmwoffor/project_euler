# Project Euler #10
# Find the sum of all prime numbers less than 2,000,000

def is_prime(n): # from wikipedia (Primality Test)
    if n<= 1:
        return False
    elif n <= 3: # 2 and 3 are prime
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i*i <= n:
        if n % i == 0 or n % (i+2) == 0:
            return False
        i = i + 6
    return True

n = 2000000
ps = 2 # already account for 2, prime sum
factor = 3

# can increment by two since all prime numbers are odd
for i in range(3,n,2):
    if is_prime(i) == True:
        ps += i
        #print(ps) # for troubleshooting
print(ps)
