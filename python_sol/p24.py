# Project Euler 24
# What is the millionth lexicographic permutation of the digits 0,1,2,3,4,5,6,7,8,9?

from itertools import permutations
# great module, returns "successive r length permutations of elements in the iterable"
lp = [''.join(n) for n in permutations('0123456789')]

print(lp[999999])
