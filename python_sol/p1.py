#!/bin/python3

import sys
import math

t = int(input().strip())
N = []
for a0 in range(t):
    N.append(int(input().strip()))

n3 = []
n5 = []
n15 = [] # don't want to double count multiples of both 3 and 5 so will get rid of multiples of 15

for i in N:
    if i % 3 != 0:
        n3.append(math.floor(i/3))
    else:
        n3.append(int((i/3)-1))
    if i % 5 != 0:
        n5.append(math.floor(i/5))
    else:
        n5.append(int((i/5)-1))
    if i % 15 != 0:
        n15.append(math.floor(i/15))
    else:
        n15.append(int((i/15)-1))


#print(n3, n5, n15)
# performing a bitwise right shift (>>1) is equivalent to dividing by two
# is necessary to avoid rounding errors when dividing by big integers
for j in range(t):
    sum3 = (n3[j]*(6+(n3[j]-1)*3)) >> 1
    #print(sum3)
    sum5 = (n5[j]*(10+(n5[j]-1)*5)) >> 1
    #print(sum5)
    sum15 = (n15[j]*(30+(n15[j]-1)*15)) >> 1
    #print(sum15)
    print(sum3+sum5-sum15)
