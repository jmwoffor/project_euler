# Project Euler 23
# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers
# An abundant number is one where the sum of its proper divisors exceeds n
# All integers greater than 28123 can be written as the sum of two abundant numbers
# 12 is the smallest abundant number, and 24 is the smallest number that is the sum of two abundant numbers
import math

def is_abundant(n): # tests if a number is abundant
    divisors = set()
    divisors.add(1)
    for i in range(2,math.ceil(n**(1/2))+1): # catches perfect numbers
        if n % i == 0:
            divisors.add(i)
            divisors.add(n//i)
    if sum(divisors) > n:
        #print(divisors)
        return True
    else:
        #print(divisors)
        return False

abundants = []
# least abundant number is 12
for i in range(12,28124):
    if is_abundant(i) == True:
        abundants.append(i)

comp_list = set(range(28124))
abundant_sums = set()
for i in abundants:
    for j in range(len(abundants)):
        # since all numbers above 28123 can be the sum of abundant numbers, cut it off there to make more efficient
        if i + abundants[j] <= 28123:
            abundant_sums.add(i + abundants[j])

nonabs = comp_list.difference(abundant_sums) # gets all positve integers that aren't the sum of abundant numbers
#print(nonabs)
print(sum(nonabs))
