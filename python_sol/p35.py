# Project Euler # 35
# How many circular primes are there below one million?
# A circular prime is a number where all rotations of the digits are themselves prime

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

def digit_rotation(n):
    digits = [d for d in str(n)]
    l = len(digits)
    rotations = [n]
    if len(digits) > 1: # don't need to rotate digits for 1-9
        while len(rotations) <  len(digits): # there should be as many rotations as digits
            leftover = "".join(digits[:l-1])
            working = int(digits[-1])*10**(l-1)+int(leftover) # take last number and add (length-1) 0's then add the leftover numbers
            rotations.append(working)
            digits = [d for d in str(working)] # sets new number to rotate
    return rotations

i = 3
circular_primes = {2} # counting 2
while i < 1000000:
    count = 0
    if is_prime(i) == True:
        rot = digit_rotation(i)
        #print(rot)
        for j in rot:
            if is_prime(j) == True:
                count += 1
                continue
            else:
                break
    if count == len(str(i)):
        #print(i)
        circular_primes.add(i)
    i += 2
print(len(circular_primes))
