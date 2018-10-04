# Project Euler #4
# Find the largest palindrome number that is the multiple of three-digit numbers

num = 999
palin = []

while num > 100:
    for i in range(100, num):
        prod = num*i
        test = str(prod)
        if test == test[::-1]:
            palin.append(int(test))
    num -= 1

print(max(palin))
