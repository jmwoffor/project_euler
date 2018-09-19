# Project Euler 16
# What is the sum of the digits of the number 2^1000

pow = str(2**1000)
sum = 0

for i in range(len(pow)):
    sum += int(pow[i])

print(sum)
