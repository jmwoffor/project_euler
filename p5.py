# Project Euler #5
# What is the smallest possible number that is divisible by all integers 1-20

n = 20
i = 1

while i <= 20:
    if n % i == 0:
        i += 1
    else:
        i = 1
        n += 1

print(n)

# you can just multiply all the numbers together you dummy
